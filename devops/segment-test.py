
#!/usr/bin/env python3

import argparse
import csv
import json
import socket
import ipaddress
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_TIMEOUT = 2.0

def load_policy(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

def validate_policy(policy):
    allowed_networks = [
        ipaddress.ip_network(net, strict=False)
        for net in policy["authorized_destinations"]
    ]

    for test in policy["tests"]:
        address = ipaddress.ip_address(test["destination"])

        if not any(address in net for net in allowed_networks):
            raise ValueError(
                f"Destination not authorized: {address}"
            )

        port = test["port"]
        if not isinstance(port, int) or not 1 <= port <= 65535:
            raise ValueError(f"Invalid port: {port}")

        if not isinstance(test["expected_open"], bool):
            raise ValueError("expected_open must be boolean")

def tcp_check(host, port, timeout):
    try:
        with socket.create_connection(
            (host, port),
            timeout=timeout
        ):
            return "OPEN", None

    except ConnectionRefusedError:
        return "REFUSED", None

    except socket.timeout:
        return "TIMEOUT", None

    except OSError as error:
        return "ERROR", str(error)

def run_tests(policy, timeout):
    results = []

    for test in policy["tests"]:
        host = test["destination"]
        port = test["port"]
        expected_open = test["expected_open"]

        status, error = tcp_check(host, port, timeout)

        observed_open = status == "OPEN"

        # Only confirmed open connections prove reachability.
        if expected_open:
            passed = status == "OPEN"
        else:
            passed = status in ("REFUSED", "TIMEOUT")

        result = {
            "source_zone": policy["source_zone"],
            "destination": host,
            "port": port,
            "expected_open": expected_open,
            "observed_status": status,
            "result": (
                "PASS" if passed else "FAIL"
            ),
            "error": error
        }

        results.append(result)

        print(
            f"[{result['result']}] "
            f"{host}:{port} "
            f"status={status}"
        )

    return results

def export_reports(results, prefix):
    timestamp = datetime.now(
        timezone.utc
    ).strftime("%Y%m%d_%H%M%S")

    json_file = Path(f"{prefix}_{timestamp}.json")
    csv_file = Path(f"{prefix}_{timestamp}.csv")

    json_file.write_text(
        json.dumps(results, indent=2),
        encoding="utf-8"
    )

    if results:
        with csv_file.open(
            "w", newline="", encoding="utf-8"
        ) as file:
            writer = csv.DictWriter(
                file,
                fieldnames=results[0].keys()
            )
            writer.writeheader()
            writer.writerows(results)

    print(f"\nJSON report: {json_file}")
    print(f"CSV report:  {csv_file}")

def main():
    parser = argparse.ArgumentParser(
        description="Basic PCI network segmentation test"
    )

    parser.add_argument(
        "--policy",
        required=True,
        help="JSON policy configuration"
    )

    parser.add_argument(
        "--timeout",
        type=float,
        default=DEFAULT_TIMEOUT
    )

    parser.add_argument(
        "--output",
        default="pci_segmentation"
    )

    args = parser.parse_args()

    if not 0 < args.timeout <= 10:
        parser.error("Timeout must be between 0 and 10 seconds")

    policy = load_policy(args.policy)
    validate_policy(policy)

    results = run_tests(policy, args.timeout)
    export_reports(results, args.output)

    failures = sum(
        result["result"] == "FAIL"
        for result in results
    )

    print("\n===== PCI SEGMENTATION SUMMARY =====")
    print(f"Total tests: {len(results)}")
    print(f"Passed: {len(results) - failures}")
    print(f"Failed: {failures}")

    raise SystemExit(1 if failures else 0)

if __name__ == "__main__":
    main()
