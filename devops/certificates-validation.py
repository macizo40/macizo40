
import ssl
import socket
import smtplib
import logging
from datetime import datetime, timezone
from email.mime.text import MIMEText

# =====================================
# CONFIGURATION
# =====================================

HOSTS = [
    ("google.com", 443),
    ("github.com", 443),
    ("yourdomain.com", 443),
]

ALERT_DAYS = [30, 15, 7, 3, 1]

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USER = "alerts@yourdomain.com"
SMTP_PASSWORD = "YOUR_APP_PASSWORD"
ALERT_EMAIL = "admin@yourdomain.com"

logging.basicConfig(
    filename="certificate_monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# =====================================
# CERTIFICATE VALIDATION
# =====================================

def check_certificate(host, port):

    try:
        context = ssl.create_default_context()

        with socket.create_connection(
            (host, port), timeout=10
        ) as sock:

            with context.wrap_socket(
                sock, server_hostname=host
            ) as secure_socket:

                cert = secure_socket.getpeercert()

        expiration = datetime.strptime(
            cert["notAfter"],
            "%b %d %H:%M:%S %Y %Z"
        ).replace(tzinfo=timezone.utc)

        now = datetime.now(timezone.utc)
        days_remaining = (expiration - now).days

        return {
            "host": host,
            "port": port,
            "expiration": expiration,
            "days_remaining": days_remaining,
            "status": "EXPIRED" if expiration <= now else "VALID"
        }

    except Exception as error:
        logging.error(f"{host}:{port} - {error}")

        return {
            "host": host,
            "port": port,
            "status": "ERROR",
            "error": str(error)
        }

# =====================================
# EMAIL ALERT
# =====================================

def send_alert(subject, message):

    email = MIMEText(message)
    email["Subject"] = subject
    email["From"] = SMTP_USER
    email["To"] = ALERT_EMAIL

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(email)

# =====================================
# MAIN MONITORING
# =====================================

def monitor_certificates():

    for host, port in HOSTS:

        result = check_certificate(host, port)

        print(result)

        if result["status"] == "ERROR":
            send_alert(
                f"SSL CHECK FAILED: {host}",
                f"Unable to validate certificate:\n{result['error']}"
            )
            continue

        days = result["days_remaining"]

        logging.info(
            f"{host} expires in {days} days"
        )

        if days <= 0:
            severity = "CRITICAL - EXPIRED"
        elif days <= 7:
            severity = "CRITICAL"
        elif days <= 15:
            severity = "HIGH"
        elif days <= 30:
            severity = "WARNING"
        else:
            severity = None

        if severity:
            message = f"""
SSL CERTIFICATE ALERT

Hostname: {host}
Port: {port}
Expiration: {result['expiration']}
Days remaining: {days}
Severity: {severity}

Action required:
Renew the SSL/TLS certificate.
"""

            send_alert(
                f"{severity}: Certificate {host}",
                message
            )


if __name__ == "__main__":
    monitor_certificates()
