
#!/usr/bin/env python3
"""
Internet Connectivity Monitor for distributed sites in Mexico.

Run this agent on multiple authorized monitoring machines.
Results are written to CSV for centralized collection and analysis.
"""

import csv
import os
import socket
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone

# Set SITE_NAME differently on each monitoring machine.
SITE_NAME = os.getenv("SITE_NAME", "unknown-site")

INTERVAL_SECONDS = 60
TIMEOUT_SECONDS = 8
OUTPUT_FILE = "internet_connectivity.csv"

TARGETS = [
    {"name": "Cloudflare", "url": "https://www.cloudflare.com/"},
    {"name": "Google", "url": "https://www.google.com/generate_204"},
    {"name": "Microsoft", "url": "https://www.microsoft.com/"},
    {"name": "Amazon", "url": "https://www.amazon.com/"},
]


def check_target(target):
    """Check DNS resolution and HTTPS reachability."""
    name = target["name"]
    url = target["url"]
    hostname = url.split("/")[2].split(":")[0]

    result = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "site": SITE_NAME,
        "target": name,
        "hostname": hostname,
        "dns_ok": False,
        "http_ok": False,
        "status_code": "",
        "latency_ms": "",
        "error": "",
    }

    try:
        socket.getaddrinfo(hostname, 443, type=socket.SOCK_STREAM)
        result["dns_ok"] = True
    except socket.gaierror as exc:
        result["error"] = f"DNS failure: {exc}"
        return result

    request = urllib.request.Request(
        url,
        headers={"User-Agent": "MexicoConnectivityMonitor/1.0"},
    )

    start = time.perf_counter()

    try:
        with urllib.request.urlopen(
            request, timeout=TIMEOUT_SECONDS
        ) as response:
            result["status_code"] = response.status
            result["http_ok"] = 200 <= response.status < 400

    except urllib.error.HTTPError as exc:
        # An HTTP response still proves that the endpoint was reached.
        result["status_code"] = exc.code
        result["http_ok"] = True
        result["error"] = f"HTTP status {exc.code}"

    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        result["error"] = str(exc)

    finally:
        result["latency_ms"] = round(
            (time.perf_counter() - start) * 1000, 2
        )

    return result


def save_results(results):
    """Append measurements to a CSV file."""
    fields = [
        "timestamp", "site", "target", "hostname",
        "dns_ok", "http_ok", "status_code",
        "latency_ms", "error",
    ]

    file_exists = (
        os.path.exists(OUTPUT_FILE)
        and os.path.getsize(OUTPUT_FILE) > 0
    )

    with open(OUTPUT_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)

        if not file_exists:
            writer.writeheader()

        writer.writerows(results)


def main():
    print(f"Monitoring site: {SITE_NAME}")
    print(f"Results file: {OUTPUT_FILE}")
    print("Press Ctrl+C to stop.\n")

    try:
        while True:
            cycle_start = time.monotonic()
            results = []

            with ThreadPoolExecutor(max_workers=len(TARGETS)) as pool:
                futures = [
                    pool.submit(check_target, target)
                    for target in TARGETS
                ]

                for future in as_completed(futures):
                    results.append(future.result())

            save_results(results)

            for result in sorted(results, key=lambda r: r["target"]):
                state = (
                    "UP" if result["http_ok"] else "DOWN"
                )
                print(
                    f"{result['timestamp']} | "
                    f"{result['site']} | {result['target']} | "
                    f"{state} | {result['latency_ms']} ms | "
                    f"{result['error']}"
                )

            elapsed = time.monotonic() - cycle_start
            time.sleep(max(0, INTERVAL_SECONDS - elapsed))

    except KeyboardInterrupt:
        print("\nMonitoring stopped.")


if __name__ == "__main__":
    main()
