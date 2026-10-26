
#!/usr/bin/env python3
"""
Read-only NTP audit for Linux virtual machines over SSH.

Supports:
  - chrony / chronyd
  - systemd-timesyncd
  - ntpd

Input:  vms.csv
Output: ntp_audit_report.csv
"""

import csv
import re
import sys
from datetime import datetime, timezone

import paramiko


INVENTORY = "vms.csv"
REPORT = "ntp_audit_report.csv"
CONNECT_TIMEOUT = 10

# Fixed, read-only commands; no inventory values are interpolated.
COMMANDS = {
    "timedatectl": "timedatectl show",
    "chrony_tracking": "chronyc tracking",
    "chrony_sources": "chronyc -n sources",
    "ntpq": "ntpq -pn",
    "services": (
        "for s in chronyd chrony systemd-timesyncd ntpd; do "
        "if command -v systemctl >/dev/null 2>&1; then "
        "systemctl is-active \"$s\" 2>/dev/null | "
        "sed \"s|^|${s}=|\"; fi; done"
    ),
    "timesync_status": "timedatectl timesync-status",
}


def run_command(ssh, command):
    """Run a read-only command and return stdout and stderr."""
    _, stdout, stderr = ssh.exec_command(
        command, timeout=CONNECT_TIMEOUT
    )
    out = stdout.read().decode("utf-8", errors="replace").strip()
    err = stderr.read().decode("utf-8", errors="replace").strip()
    return out, err


def parse_properties(output):
    properties = {}
    for line in output.splitlines():
        if "=" in line:
            key, value = line.split("=", 1)
            properties[key.strip()] = value.strip()
    return properties


def audit_vm(vm):
    host = vm["host"].strip()
    username = vm["username"].strip()
    port = int(vm.get("port") or 22)

    result = {
        "host": host,
        "username": username,
        "reachable": "NO",
        "service": "UNKNOWN",
        "ntp_configured": "UNKNOWN",
        "synchronized": "UNKNOWN",
        "ntp_source": "",
        "time_offset": "",
        "compliance": "UNKNOWN",
        "details": "",
    }

    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    # Unknown host keys are rejected: provision trusted SSH host keys first.
    ssh.set_missing_host_key_policy(paramiko.RejectPolicy())

    try:
        ssh.connect(
            hostname=host,
            port=port,
            username=username,
            timeout=CONNECT_TIMEOUT,
            banner_timeout=CONNECT_TIMEOUT,
            auth_timeout=CONNECT_TIMEOUT,
            allow_agent=True,
            look_for_keys=True,
        )

        result["reachable"] = "YES"

        timedate, _ = run_command(ssh, COMMANDS["timedatectl"])
        tracking, tracking_err = run_command(
            ssh, COMMANDS["chrony_tracking"]
        )
        sources, _ = run_command(
            ssh, COMMANDS["chrony_sources"]
        )
        ntpq, _ = run_command(ssh, COMMANDS["ntpq"])
        services, _ = run_command(ssh, COMMANDS["services"])
        timesync, _ = run_command(
            ssh, COMMANDS["timesync_status"]
        )

        props = parse_properties(timedate)
        active_services = [
            line.split("=", 1)[0]
            for line in services.splitlines()
            if "=" in line
            and line.split("=", 1)[1].strip() == "active"
        ]

        result["service"] = (
            ",".join(active_services) if active_services else "NONE"
        )

        # Detect synchronization state.
        sync_value = props.get("NTPSynchronized", "").lower()
        chrony_leap = re.search(
            r"Leap status:\s*(.+)", tracking, re.IGNORECASE
        )
        chrony_synced = bool(
            chrony_leap
            and chrony_leap.group(1).strip().lower() == "normal"
        )

        ntpq_lines = [
            line for line in ntpq.splitlines()
            if line.startswith("*")
        ]
        chrony_selected = any(
            line.startswith("^*") for line in sources.splitlines()
        )

        synchronized = (
            sync_value == "yes"
            or chrony_synced
            or bool(ntpq_lines)
        )

        # A running client alone does not prove synchronization.
        if synchronized:
            result["synchronized"] = "YES"
        elif (
            sync_value == "no"
            or "false" == sync_value
            or chrony_leap
        ):
            result["synchronized"] = "NO"
        else:
            result["synchronized"] = "UNKNOWN"

        # Detect configured/available sources.
        source_lines = [
            line.strip() for line in sources.splitlines()
            if line.strip().startswith(("^", "=", "#"))
        ]

        server_match = re.search(
            r"Server:\s*(\S+)", timesync, re.IGNORECASE
        )
        ref_match = re.search(
            r"Reference ID\s*:\s*(.+)", tracking, re.IGNORECASE
        )

        if chrony_selected:
            result["ntp_source"] = next(
                line for line in source_lines
                if line.startswith("^*")
            )
        elif ntpq_lines:
            result["ntp_source"] = ntpq_lines[0].split()[1]
        elif server_match:
            result["ntp_source"] = server_match.group(1)
        elif ref_match:
            result["ntp_source"] = ref_match.group(1).strip()

        if source_lines or ntpq_lines or server_match:
            result["ntp_configured"] = "YES"
        elif props.get("NTP", "").lower() == "yes":
            result["ntp_configured"] = "YES"
        elif (
            "systemd-timesyncd" in active_services
            or "chronyd" in active_services
            or "chrony" in active_services
            or "ntpd" in active_services
        ):
            result["ntp_configured"] = "UNKNOWN"
        else:
            result["ntp_configured"] = "NO"

        offset_match = re.search(
            r"System time\s*:\s*(.+)", tracking, re.IGNORECASE
        )
        if offset_match:
            result["time_offset"] = offset_match.group(1).strip()

        if (
            result["synchronized"] == "YES"
            and result["ntp_configured"] == "YES"
        ):
            result["compliance"] = "COMPLIANT"
        elif result["synchronized"] == "NO":
            result["compliance"] = "NONCOMPLIANT"
        else:
            result["compliance"] = "REVIEW"

        if result["synchronized"] == "UNKNOWN":
            result["details"] = (
                "Could not establish synchronization state; "
                "check installed NTP client and command permissions."
            )
        elif result["synchronized"] == "NO":
            result["details"] = (
                "No confirmed synchronization; check NTP service, "
                "server reachability, UDP/123, and system logs."
            )

    except Exception as exc:
        result["details"] = (
            f"{type(exc).__name__}: {exc}"
        )
    finally:
        ssh.close()

    return result


def main():
    try:
        with open(INVENTORY, newline="", encoding="utf-8") as f:
            vms = list(csv.DictReader(f))
    except OSError as exc:
        sys.exit(f"Cannot read {INVENTORY}: {exc}")

    if not vms:
        sys.exit("Inventory is empty.")

    fields = [
        "host", "username", "reachable", "service",
        "ntp_configured", "synchronized", "ntp_source",
        "time_offset", "compliance", "details",
    ]

    results = []
    for vm in vms:
        print(f"Checking {vm.get('host', '<unknown>')}...")
        results.append(audit_vm(vm))

    with open(REPORT, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(results)

    compliant = sum(
        r["compliance"] == "COMPLIANT" for r in results
    )
    noncompliant = sum(
        r["compliance"] == "NONCOMPLIANT" for r in results
    )
    review = sum(
        r["compliance"] == "REVIEW"
        or r["compliance"] == "UNKNOWN"
        for r in results
    )

    print("\n--- NTP Audit Summary ---")
    print(f"Timestamp (UTC): {datetime.now(timezone.utc).isoformat()}")
    print(f"VMs checked:    {len(results)}")
    print(f"Compliant:      {compliant}")
    print(f"Noncompliant:   {noncompliant}")
    print(f"Needs review:   {review}")
    print(f"Report:         {REPORT}")


if __name__ == "__main__":
    main()
