#!/usr/bin/env python3
"""Read-only scanner for possible PCI account-data exposure in log files.

Reports locations and non-reversible fingerprints. It never writes raw matches.
Exit codes: 0 = clean, 1 = operational error, 2 = possible PCI data found.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import hmac
import json
import os
import re
import sys
from collections import Counter
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, TextIO


PAN_CANDIDATE = re.compile(r"(?<!\d)(?:\d[ -]?){12,18}\d(?!\d)")
LABELED_CVV = re.compile(
    r"(?i)\b(?:cvv2?|cvc2?|cid|security[ _-]?code|card[ _-]?verification)\b"
    r"\s*[:=]\s*[\"']?(\d{3,4})\b"
)
LABELED_EXPIRY = re.compile(
    r"(?i)\b(?:exp(?:iry|iration)?(?:[ _-]?date)?|expires)\b\s*[:=]\s*[\"']?"
    r"((?:0?[1-9]|1[0-2])(?:[/ -]|%2F)(?:\d{2}|20\d{2}))\b"
)
TRACK1 = re.compile(r"%B\d{13,19}\^[^^\r\n]{1,26}\^[0-9]{7,}[^?\r\n]*\?")
TRACK2 = re.compile(r";\d{13,19}=\d{7,}[^?\r\n]*\?")
LABELED_PIN = re.compile(
    r"(?i)\b(?:pin(?:[ _-]?block)?|encrypted[ _-]?pin)\b\s*[:=]\s*[\"']?([0-9A-F]{4,32})\b"
)
LABELED_SERVICE_CODE = re.compile(
    r"(?i)\bservice[ _-]?code\b\s*[:=]\s*[\"']?(\d{3})\b"
)

DEFAULT_SUFFIXES = {
    ".log", ".txt", ".out", ".json", ".jsonl", ".csv", ".tsv", ".xml",
    ".gz", ".trace",
}


@dataclass(frozen=True)
class Finding:
    file: str
    line: int
    column: int
    data_type: str
    severity: str
    fingerprint: str
    masked_value: str | None = None


def luhn_valid(digits: str) -> bool:
    if not 13 <= len(digits) <= 19 or len(set(digits)) == 1:
        return False
    total = 0
    parity = len(digits) % 2
    for index, char in enumerate(digits):
        value = int(char)
        if index % 2 == parity:
            value *= 2
            if value > 9:
                value -= 9
        total += value
    return total % 10 == 0


def fingerprint(secret: str, key: bytes) -> str:
    return hmac.new(key, secret.encode("utf-8"), hashlib.sha256).hexdigest()[:16]


def mask_pan(digits: str) -> str:
    return f"{'*' * max(0, len(digits) - 4)}{digits[-4:]}"


def findings_for_line(path: Path, number: int, line: str, key: bytes) -> list[Finding]:
    findings: list[Finding] = []
    occupied: list[tuple[int, int]] = []

    for match in PAN_CANDIDATE.finditer(line):
        digits = re.sub(r"\D", "", match.group())
        if luhn_valid(digits):
            findings.append(Finding(
                str(path), number, match.start() + 1, "PAN", "critical",
                fingerprint(digits, key), mask_pan(digits),
            ))
            occupied.append(match.span())

    patterns = [
        (TRACK1, "TRACK_1_DATA", "critical"),
        (TRACK2, "TRACK_2_DATA", "critical"),
        (LABELED_CVV, "CARD_VERIFICATION_CODE", "critical"),
        (LABELED_PIN, "PIN_OR_PIN_BLOCK", "critical"),
        (LABELED_EXPIRY, "EXPIRATION_DATE", "high"),
        (LABELED_SERVICE_CODE, "SERVICE_CODE", "high"),
    ]
    for pattern, data_type, severity in patterns:
        for match in pattern.finditer(line):
            if data_type.startswith("TRACK") and any(
                match.start() < end and match.end() > start for start, end in occupied
            ):
                # Still report track data; it is materially different from a PAN.
                pass
            secret = match.group(1) if match.lastindex else match.group()
            findings.append(Finding(
                str(path), number, match.start() + 1, data_type, severity,
                fingerprint(secret, key), None,
            ))
    return findings


def open_log(path: Path) -> TextIO:
    if path.suffix.lower() == ".gz":
        return gzip.open(path, "rt", encoding="utf-8", errors="replace")
    return path.open("r", encoding="utf-8", errors="replace")


def candidate_files(inputs: Iterable[str], all_files: bool) -> Iterable[Path]:
    seen: set[Path] = set()
    for raw in inputs:
        source = Path(raw)
        paths = source.rglob("*") if source.is_dir() else [source]
        for path in paths:
            try:
                resolved = path.resolve()
            except OSError:
                continue
            if resolved in seen or not path.is_file() or path.is_symlink():
                continue
            if not all_files and path.suffix.lower() not in DEFAULT_SUFFIXES:
                continue
            seen.add(resolved)
            yield path


def scan_file(path: Path, key: bytes, max_bytes: int) -> tuple[list[Finding], str | None]:
    try:
        if path.stat().st_size > max_bytes:
            return [], f"skipped: exceeds {max_bytes} bytes"
        results: list[Finding] = []
        with open_log(path) as handle:
            for number, line in enumerate(handle, start=1):
                results.extend(findings_for_line(path, number, line, key))
        return results, None
    except (OSError, EOFError, gzip.BadGzipFile) as exc:
        return [], f"scan error: {type(exc).__name__}"


def run_self_test() -> None:
    key = b"self-test-key"
    synthetic_pan = "4" + ("0" * 14) + "2"
    line = f"checkout pan={synthetic_pan} cvv=123 expiration=12/30"
    results = findings_for_line(Path("synthetic.log"), 1, line, key)
    types = {item.data_type for item in results}
    assert {"PAN", "CARD_VERIFICATION_CODE", "EXPIRATION_DATE"} <= types
    serialized = json.dumps([asdict(item) for item in results])
    assert synthetic_pan not in serialized and "cvv=123" not in serialized
    assert not luhn_valid("1234567890123456")
    print("Self-test passed: detection works and raw test secrets were not reported.")


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan logs for possible PCI data exposure.")
    parser.add_argument("paths", nargs="*", help="Log files or directories to scan")
    parser.add_argument("--output", default="pci_scan_report.json", help="JSON report path")
    parser.add_argument("--all-files", action="store_true", help="Scan every file extension")
    parser.add_argument("--max-file-mb", type=int, default=100, help="Per-file limit")
    parser.add_argument(
        "--fingerprint-key-env", default="PCI_SCANNER_HMAC_KEY",
        help="Environment variable containing a stable HMAC key",
    )
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        run_self_test()
        return 0
    if not args.paths:
        parser.error("provide at least one log file or directory")
    if args.max_file_mb < 1:
        parser.error("--max-file-mb must be at least 1")

    configured_key = os.environ.get(args.fingerprint_key_env)
    key = configured_key.encode() if configured_key else os.urandom(32)
    findings: list[Finding] = []
    errors: list[dict[str, str]] = []
    scanned = 0

    for path in candidate_files(args.paths, args.all_files):
        scanned += 1
        file_findings, error = scan_file(path, key, args.max_file_mb * 1024 * 1024)
        findings.extend(file_findings)
        if error:
            errors.append({"file": str(path), "message": error})

    counts = Counter(item.data_type for item in findings)
    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "files_scanned": scanned,
        "finding_count": len(findings),
        "counts_by_type": dict(sorted(counts.items())),
        "findings": [asdict(item) for item in findings],
        "errors": errors,
        "notes": [
            "Raw matches are never included; PANs are masked and all matches are fingerprinted.",
            "Results are indicators requiring review, not proof of PCI DSS compliance.",
            "Cardholder names alone are not detected because reliable identification requires context.",
        ],
    }
    Path(args.output).write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"Scanned {scanned} files; found {len(findings)} indicators.")
    print(f"Report: {args.output}")
    if errors:
        print(f"Warnings/skips: {len(errors)}", file=sys.stderr)
    return 2 if findings else (1 if errors and scanned == 0 else 0)


if __name__ == "__main__":
    raise SystemExit(main())
