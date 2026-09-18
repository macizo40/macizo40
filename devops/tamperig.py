#!/usr/bin/env python3

import hashlib
import json
import argparse
from pathlib import Path
from datetime import datetime

BASELINE_FILE = "file_integrity_baseline.json"


def sha256_file(file_path):
    """Calculate the SHA-256 hash of a file."""
    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:
            while chunk := file.read(8192):
                sha256.update(chunk)

        return sha256.hexdigest()

    except (PermissionError, OSError) as error:
        print(f"[ERROR] Cannot read {file_path}: {error}")
        return None


def scan_directory(directory):
    """Return hashes for all files under a directory."""
    results = {}

    directory = Path(directory).resolve()
    baseline_path = Path(BASELINE_FILE).resolve()

    for file_path in directory.rglob("*"):

        if not file_path.is_file():
            continue

        # Don't monitor the baseline itself
        if file_path.resolve() == baseline_path:
            continue

        file_hash = sha256_file(file_path)

        if file_hash:
            relative_path = str(file_path.relative_to(directory))
            results[relative_path] = file_hash

    return results


def create_baseline(directory):
    """Create the trusted baseline."""
    hashes = scan_directory(directory)

    baseline = {
        "created": datetime.now().isoformat(),
        "directory": str(Path(directory).resolve()),
        "files": hashes
    }

    with open(BASELINE_FILE, "w") as file:
        json.dump(baseline, file, indent=4)

    print(f"[OK] Baseline created: {BASELINE_FILE}")
    print(f"[OK] Files monitored: {len(hashes)}")


def check_integrity(directory):
    """Compare current files against the trusted baseline."""

    baseline_path = Path(BASELINE_FILE)

    if not baseline_path.exists():
        print("[ERROR] Baseline does not exist.")
        print("Run the program with --init first.")
        return

    with open(baseline_path, "r") as file:
        baseline = json.load(file)

    original = baseline["files"]
    current = scan_directory(directory)

    tampering_detected = False

    # Modified or deleted files
    for file_path, original_hash in original.items():

        if file_path not in current:
            print(f"[DELETED]  {file_path}")
            tampering_detected = True

        elif current[file_path] != original_hash:
            print(f"[MODIFIED] {file_path}")
            tampering_detected = True

    # New files
    for file_path in current:

        if file_path not in original:
            print(f"[NEW]      {file_path}")
            tampering_detected = True

    if tampering_detected:
        print("\n[WARNING] Possible file tampering detected!")
    else:
        print("\n[OK] No file tampering detected.")


def main():

    parser = argparse.ArgumentParser(
        description="File Integrity / Tampering Detection Tool"
    )

    parser.add_argument(
        "directory",
        help="Directory containing files to monitor"
    )

    parser.add_argument(
        "--init",
        action="store_true",
        help="Create the initial trusted baseline"
    )

    args = parser.parse_args()

    if args.init:
        create_baseline(args.directory)
    else:
        check_integrity(args.directory)


if __name__ == "__main__":
    main()