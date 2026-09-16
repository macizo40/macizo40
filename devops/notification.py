"""
maintenance_notifier.py

Automatically sends notifications around a planned maintenance window.

Example:
    Maintenance: Database upgrade
    Start:       2026-09-20 22:00
    End:         2026-09-21 01:00

Notifications:
    - 24 hours before
    - 1 hour before
    - At maintenance start
    - Every 30 minutes during maintenance
    - At maintenance completion
"""

import time
import smtplib
import requests

from dataclasses import dataclass
from datetime import datetime, timedelta
from email.message import EmailMessage
from zoneinfo import ZoneInfo


# -------------------------------------------------------
# CONFIGURATION
# -------------------------------------------------------

TIMEZONE = ZoneInfo("America/Mexico_City")

SMTP_SERVER = "smtp.company.com"
SMTP_PORT = 587
SMTP_USER = "maintenance@company.com"
SMTP_PASSWORD = "USE_SECRET_MANAGER"

EMAIL_RECIPIENTS = [
    "users@company.com",
    "service-desk@company.com"
]

WEBHOOK_URL = "https://your-notification-platform/webhook"


@dataclass
class MaintenanceWindow:
    service: str
    description: str
    start: datetime
    end: datetime
    ticket: str
    impact: str


maintenance = MaintenanceWindow(
    service="Customer Payment API",

    description=(
        "Planned database and infrastructure maintenance."
    ),

    start=datetime(
        2026, 9, 20, 22, 0,
        tzinfo=TIMEZONE
    ),

    end=datetime(
        2026, 9, 21, 1, 0,
        tzinfo=TIMEZONE
    ),

    ticket="CHG-10452",

    impact=(
        "The service may be intermittently unavailable."
    )
)


# -------------------------------------------------------
# MESSAGE GENERATOR
# -------------------------------------------------------

def build_message(status):

    if status == "24H":

        title = "Scheduled Maintenance - 24 Hour Notice"

        message = f"""
Scheduled maintenance is planned for:

Service:
{maintenance.service}

Start:
{maintenance.start:%Y-%m-%d %H:%M %Z}

Expected completion:
{maintenance.end:%Y-%m-%d %H:%M %Z}

Impact:
{maintenance.impact}

Change:
{maintenance.ticket}

Please do not open an incident ticket during this window
for the expected service interruption.
"""

    elif status == "1H":

        title = "Maintenance Starts in 1 Hour"

        message = f"""
Reminder: maintenance for {maintenance.service}
will begin in approximately one hour.

Expected maintenance window:

{maintenance.start:%H:%M} - {maintenance.end:%H:%M}

Impact:
{maintenance.impact}

Change:
{maintenance.ticket}
"""

    elif status == "START":

        title = "Maintenance In Progress"

        message = f"""
Maintenance has started for:

{maintenance.service}

Current status:
MAINTENANCE IN PROGRESS

Expected completion:
{maintenance.end:%Y-%m-%d %H:%M %Z}

Users may experience temporary service interruption.

There is no need to open an incident ticket for the
expected maintenance impact.

Change:
{maintenance.ticket}
"""

    elif status == "UPDATE":

        title = "Maintenance Status Update"

        message = f"""
Maintenance for {maintenance.service}
is still in progress.

Expected completion:

{maintenance.end:%Y-%m-%d %H:%M %Z}

Engineering teams are actively monitoring the service.

Change:
{maintenance.ticket}
"""

    elif status == "COMPLETE":

        title = "Maintenance Completed"

        message = f"""
Maintenance has been completed successfully.

Service:
{maintenance.service}

Status:
SERVICE RESTORED

Users can resume normal operations.

If you continue experiencing problems,
please open an incident with the Service Desk.

Change:
{maintenance.ticket}
"""

    else:
        raise ValueError("Unknown notification status")

    return title, message


# -------------------------------------------------------
# EMAIL
# -------------------------------------------------------

def send_email(title, message):

    email = EmailMessage()

    email["Subject"] = title
    email["From"] = SMTP_USER
    email["To"] = ", ".join(EMAIL_RECIPIENTS)

    email.set_content(message)

    try:

        with smtplib.SMTP(
            SMTP_SERVER,
            SMTP_PORT
        ) as server:

            server.starttls()

            server.login(
                SMTP_USER,
                SMTP_PASSWORD
            )

            server.send_message(email)

        print("Email notification sent.")

    except Exception as error:

        print(
            f"Email notification failed: {error}"
        )


# -------------------------------------------------------
# WEBHOOK
# -------------------------------------------------------

def send_webhook(title, message):

    payload = {
        "title": title,
        "text": message
    }

    try:

        response = requests.post(
            WEBHOOK_URL,
            json=payload,
            timeout=10
        )

        response.raise_for_status()

        print("Webhook notification sent.")

    except requests.RequestException as error:

        print(
            f"Webhook notification failed: {error}"
        )


# -------------------------------------------------------
# NOTIFICATION
# -------------------------------------------------------

def notify(status):

    title, message = build_message(status)

    print(
        f"\nSending notification: {title}"
    )

    send_email(
        title,
        message
    )

    send_webhook(
        title,
        message
    )


# -------------------------------------------------------
# MAINTENANCE SCHEDULER
# -------------------------------------------------------

def maintenance_scheduler():

    sent = set()

    while True:

        now = datetime.now(TIMEZONE)

        # 24 hours before maintenance

        if (
            maintenance.start - timedelta(hours=24)
            <= now
            < maintenance.start - timedelta(hours=23, minutes=59)
            and "24H" not in sent
        ):

            notify("24H")
            sent.add("24H")

        # 1 hour before maintenance

        if (
            maintenance.start - timedelta(hours=1)
            <= now
            < maintenance.start
            and "1H" not in sent
        ):

            notify("1H")
            sent.add("1H")

        # Maintenance start

        if (
            maintenance.start <= now < maintenance.end
            and "START" not in sent
        ):

            notify("START")
            sent.add("START")

        # Periodic updates every 30 minutes

        if maintenance.start < now < maintenance.end:

            minutes_running = int(
                (now - maintenance.start).total_seconds()
                / 60
            )

            update_number = minutes_running // 30

            update_key = f"UPDATE-{update_number}"

            if (
                update_number > 0
                and update_key not in sent
            ):

                notify("UPDATE")
                sent.add(update_key)

        # Maintenance completed

        if (
            now >= maintenance.end
            and "COMPLETE" not in sent
        ):

            notify("COMPLETE")
            sent.add("COMPLETE")

            print(
                "Maintenance notification cycle completed."
            )

            break

        time.sleep(30)


# -------------------------------------------------------
# MAIN
# -------------------------------------------------------

if __name__ == "__main__":

    print("Maintenance Notification Service")

    print(
        f"Service: {maintenance.service}"
    )

    print(
        f"Window: "
        f"{maintenance.start} -> "
        f"{maintenance.end}"
    )

    maintenance_scheduler()