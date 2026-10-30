
import socket
import ssl
import csv
import json
import subprocess
import platform
from datetime import datetime

# -----------------------------------------
# CONFIGURATION
# -----------------------------------------

TARGETS = [
    {
        "site": "Mexico-DC",
        "host": "192.168.10.10",
        "port": 443,
        "protocol": "HTTPS"
    },
    {
        "site": "AWS-US-East",
        "host": "10.20.10.10",
        "port": 443,
        "protocol": "HTTPS"
    },
    {
        "site": "Azure-West-Europe",
        "host": "example.com",
        "port": 443,
        "protocol": "HTTPS"
    },
    {
        "site": "Legacy-Server",
        "host": "192.168.10.20",
        "port": 80,
        "protocol": "HTTP"
    }
]

TIMEOUT = 5
CSV_REPORT = "encryption_audit.csv"


# -----------------------------------------
# TLS VALIDATION
# -----------------------------------------

def validate_tls(host, port):

    result = {
        "encrypted": False,
        "tls_version": None,
        "cipher": None,
        "certificate_valid": False,
        "certificate_expiration": None,
        "error": None
    }

    try:
        context = ssl.create_default_context()

        with socket.create_connection(
            (host, port), timeout=TIMEOUT
        ) as sock:

            with context.wrap_socket(
                sock, server_hostname=host
            ) as secure_socket:

                cert = secure_socket.getpeercert()

                result["encrypted"] = True
                result["tls_version"] = (
                    secure_socket.version()
                )

                cipher = secure_socket.cipher()

                if cipher:
                    result["cipher"] = cipher[0]

                result["certificate_valid"] = True

                result["certificate_expiration"] = (
                    cert.get("notAfter")
                )

    except ssl.SSLCertVerificationError as e:
        result["error"] = (
            f"Certificate validation failed: {e}"
        )

    except ssl.SSLError as e:
        result["error"] = f"TLS error: {e}"

    except Exception as e:
        result["error"] = str(e)

    return result


# -----------------------------------------
# CLEAR-TEXT PROTOCOL DETECTION
# -----------------------------------------

def check_cleartext(protocol, port):

    insecure_ports = {
        21: "FTP",
        23: "TELNET",
        80: "HTTP",
        110: "POP3",
        143: "IMAP"
    }

    if port in insecure_ports:
        return "INSECURE_PROTOCOL"

    if protocol.upper() in [
        "HTTP", "FTP", "TELNET"
    ]:
        return "INSECURE_PROTOCOL"

    return "REQUIRES_VALIDATION"


# -----------------------------------------
# CONNECTIVITY VALIDATION
# -----------------------------------------

def check_connectivity(host, port):

    try:
        with socket.create_connection(
            (host, port), timeout=TIMEOUT
        ):
            return True

    except Exception:
        return False


# -----------------------------------------
# MAIN AUDIT
# -----------------------------------------

def audit_site(target):

    host = target["host"]
    port = target["port"]
    protocol = target["protocol"]

    print(f"Checking {target['site']}...")

    connected = check_connectivity(host, port)

    tls_result = validate_tls(host, port)

    cleartext = check_cleartext(protocol, port)

    if tls_result["encrypted"]:
        status = "ENCRYPTED"
    elif cleartext == "INSECURE_PROTOCOL":
        status = "NOT_ENCRYPTED"
    elif connected:
        status = "ENCRYPTION_NOT_VERIFIED"
    else:
        status = "CONNECTION_FAILED"

    return {
        "timestamp": datetime.now().isoformat(),
        "site": target["site"],
        "host": host,
        "port": port,
        "protocol": protocol,
        "connectivity": connected,
        "encryption_status": status,
        "tls_version": tls_result["tls_version"],
        "cipher": tls_result["cipher"],
        "certificate_valid": tls_result["certificate_valid"],
        "certificate_expiration":
            tls_result["certificate_expiration"],
        "error": tls_result["error"]
    }


# -----------------------------------------
# CSV REPORT
# -----------------------------------------

def generate_report(results):

    if not results:
        return

    with open(
        CSV_REPORT, "w", newline="", encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file, fieldnames=results[0].keys()
        )

        writer.writeheader()
        writer.writerows(results)

    print(f"\nReport generated: {CSV_REPORT}")


# -----------------------------------------
# EXECUTION
# -----------------------------------------

def main():

    results = []

    print("\nSITE-TO-SITE ENCRYPTION AUDIT")
    print("=" * 45)

    for target in TARGETS:

        result = audit_site(target)

        results.append(result)

        print(
            f"{result['site']}: "
            f"{result['encryption_status']}"
        )

        if result["tls_version"]:
            print(
                f"TLS: {result['tls_version']} | "
                f"Cipher: {result['cipher']}"
            )

    generate_report(results)

    print("\nAUDIT COMPLETED")


if __name__ == "__main__":
    main()
