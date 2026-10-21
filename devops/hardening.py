
#!/usr/bin/env python3

import argparse
import json
import os
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

BACKUP_DIR = Path("/var/backups/linux-hardening")
REPORT_FILE = Path("linux_hardening_report.json")

CONFIG_FILES = {
    "ssh": "/etc/ssh/sshd_config",
    "sysctl": "/etc/sysctl.conf",
    "login": "/etc/login.defs",
    "pam": "/etc/security/pwquality.conf",
}

def run_command(command):
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=10,
            check=False
        )
        return {
            "returncode": result.returncode,
            "output": result.stdout.strip(),
            "error": result.stderr.strip()
        }
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {"error": str(exc)}

def audit_hardening():
    checks = {
        "SELinux": ["getenforce"],
        "AppArmor": ["aa-status"],
        "UFW": ["ufw", "status"],
        "Firewalld": ["firewall-cmd", "--state"],
        "Auditd": ["systemctl", "is-active", "auditd"],
        "SSH": ["sshd", "-T"],
        "Kernel": ["sysctl", "-a"],
    }

    report = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "checks": {},
        "config_files": {}
    }

    for name, command in checks.items():
        print(f"Checking {name}...")
        result = run_command(command)

        # Keep reports manageable.
        if "output" in result:
            result["output"] = result["output"][:12000]

        report["checks"][name] = result

    for name, path in CONFIG_FILES.items():
        report["config_files"][name] = {
            "path": path,
            "exists": Path(path).is_file()
        }

    REPORT_FILE.write_text(
        json.dumps(report, indent=2)
    )

    print(f"Audit saved to {REPORT_FILE}")

def backup_config(name):
    source = Path(CONFIG_FILES[name])

    if not source.is_file() or source.is_symlink():
        raise ValueError("Source must be an existing regular file")

    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    os.chmod(BACKUP_DIR, 0o700)

    timestamp = datetime.now(timezone.utc).strftime(
        "%Y%m%d_%H%M%S_%f"
    )

    destination = BACKUP_DIR / f"{name}_{timestamp}.bak"

    # Exclusive creation avoids overwriting previous backups.
    with destination.open("xb") as output:
        shutil.copyfileobj(source.open("rb"), output)

    shutil.copymode(source, destination)

    print(f"Backup created: {destination}")
    return destination

def restore_config(name, backup_path):
    source = Path(backup_path).resolve(strict=True)
    backup_root = BACKUP_DIR.resolve(strict=True)

    if source.parent != backup_root:
        raise ValueError("Backup must be inside the backup directory")

    if not source.name.startswith(f"{name}_"):
        raise ValueError("Backup does not match selected configuration")

    if not source.is_file():
        raise ValueError("Invalid backup")

    target = Path(CONFIG_FILES[name])

    # Preserve current configuration before restoration.
    backup_config(name)

    shutil.copy2(source, target)
    print(f"Restored {target} from {source}")
    print("Validate configuration before restarting services.")

def main():
    parser = argparse.ArgumentParser(
        description="Linux hardening audit and controlled rollback"
    )

    parser.add_argument(
        "action",
        choices=["audit", "backup", "restore"]
    )

    parser.add_argument(
        "--config",
        choices=CONFIG_FILES.keys()
    )

    parser.add_argument("--backup-file")

    args = parser.parse_args()

    if args.action == "audit":
        audit_hardening()

    elif args.action == "backup":
        if not args.config:
            parser.error("--config is required")
        backup_config(args.config)

    elif args.action == "restore":
        if not args.config or not args.backup_file:
            parser.error(
                "--config and --backup-file are required"
            )
        restore_config(args.config, args.backup_file)

if __name__ == "__main__":
    main()
