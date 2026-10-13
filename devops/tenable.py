
import os
import csv
import time
import requests
from collections import Counter

BASE_URL = "https://cloud.tenable.com"

ACCESS_KEY = os.environ["TENABLE_ACCESS_KEY"]
SECRET_KEY = os.environ["TENABLE_SECRET_KEY"]

HEADERS = {
    "X-ApiKeys": (
        f"accessKey={ACCESS_KEY};"
        f"secretKey={SECRET_KEY}"
    ),
    "Accept": "application/json",
    "Content-Type": "application/json"
}

SEVERITY = {
    0: "INFO",
    1: "LOW",
    2: "MEDIUM",
    3: "HIGH",
    4: "CRITICAL"
}


def cvss_classification(score):
    if score is None:
        return "UNKNOWN"

    score = float(score)

    if score >= 9.0:
        return "CRITICAL"
    elif score >= 7.0:
        return "HIGH"
    elif score >= 4.0:
        return "MEDIUM"
    elif score > 0:
        return "LOW"
    return "NONE"


def tenable_request(method, endpoint, **kwargs):
    response = requests.request(
        method,
        BASE_URL + endpoint,
        headers=HEADERS,
        timeout=60,
        **kwargs
    )

    response.raise_for_status()
    return response.json() if response.content else {}


def create_export():
    payload = {
        "num_assets": 500,
        "filters": {
            "state": ["OPEN", "REOPENED"]
        }
    }

    result = tenable_request(
        "POST",
        "/vulns/export",
        json=payload
    )

    return result["export_uuid"]


def wait_for_export(export_uuid):
    while True:
        status = tenable_request(
            "GET",
            f"/vulns/export/{export_uuid}/status"
        )

        state = status.get("status")

        if state == "FINISHED":
            return status.get("chunks_available", [])

        if state in ("ERROR", "CANCELLED"):
            raise RuntimeError(
                f"Export failed: {state}"
            )

        print("Waiting for Tenable export...")
        time.sleep(5)


def get_vulnerabilities():
    export_uuid = create_export()
    chunks = wait_for_export(export_uuid)

    for chunk in chunks:
        data = tenable_request(
            "GET",
            f"/vulns/export/{export_uuid}/chunks/{chunk}"
        )

        for vulnerability in data:
            yield vulnerability


def analyze_vulnerabilities():
    results = []
    summary = Counter()

    for vuln in get_vulnerabilities():
        plugin = vuln.get("plugin") or {}
        asset = vuln.get("asset") or {}

        severity_id = vuln.get("severity", 0)
        severity = SEVERITY.get(
            severity_id, "UNKNOWN"
        )

        cvss_score = plugin.get("cvss3_base_score")
        if cvss_score is None:
            cvss_score = plugin.get("cvss_base_score")

        cvss_level = cvss_classification(cvss_score)

        record = {
            "asset_id": asset.get("uuid", ""),
            "hostname": asset.get("hostname", ""),
            "plugin_id": plugin.get("id", ""),
            "plugin_name": plugin.get("name", ""),
            "severity": severity,
            "cvss_score": cvss_score,
            "cvss_classification": cvss_level,
            "state": vuln.get("state", ""),
            "first_found": vuln.get("first_found", ""),
            "last_found": vuln.get("last_found", "")
        }

        results.append(record)
        summary[severity] += 1

    return results, summary


def export_csv(records, filename):
    if not records:
        print("No vulnerabilities found.")
        return

    with open(
        filename,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=records[0].keys()
        )

        writer.writeheader()
        writer.writerows(records)


def main():
    print("Connecting to Tenable...")

    records, summary = analyze_vulnerabilities()

    print("\nVULNERABILITY SUMMARY")
    print("-" * 35)

    for severity in [
        "CRITICAL",
        "HIGH",
        "MEDIUM",
        "LOW",
        "INFO"
    ]:
        print(
            f"{severity:10}: "
            f"{summary[severity]}"
        )

    print("-" * 35)
    print(f"TOTAL: {len(records)}")

    export_csv(
        records,
        "tenable_vulnerabilities.csv"
    )

    print("\nAnalysis completed.")


if __name__ == "__main__":
    main()
