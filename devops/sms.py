
import os
import argparse
import logging
from dotenv import load_dotenv
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class NotificationService:

    def __init__(self):
        self.client = Client(
            os.environ["TWILIO_ACCOUNT_SID"],
            os.environ["TWILIO_AUTH_TOKEN"]
        )

        self.sms_sender = os.environ["TWILIO_SMS_FROM"]
        self.whatsapp_sender = os.environ["TWILIO_WHATSAPP_FROM"]

    def send(self, phone, message, channel="sms"):
        """Send an SMS or WhatsApp notification."""

        if channel not in ("sms", "whatsapp"):
            raise ValueError("Channel must be sms or whatsapp")

        phone = phone.strip()

        if not phone.startswith("+"):
            raise ValueError(
                "Phone number must use E.164 format"
            )

        if channel == "whatsapp":
            sender = self.whatsapp_sender
            recipient = f"whatsapp:{phone}"
        else:
            sender = self.sms_sender
            recipient = phone

        try:
            result = self.client.messages.create(
                body=message,
                from_=sender,
                to=recipient
            )

            logging.info(
                "Notification accepted: channel=%s SID=%s",
                channel,
                result.sid
            )

            return {
                "success": True,
                "sid": result.sid,
                "status": result.status
            }

        except TwilioRestException as error:
            logging.error(
                "Notification failed: code=%s",
                error.code
            )

            return {
                "success": False,
                "error_code": error.code
            }

    def send_bulk(self, recipients, message, channel):
        """Send notifications to a list of recipients."""

        results = []

        for phone in recipients:
            result = self.send(phone, message, channel)
            results.append(result)

        return results


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="SMS / WhatsApp Notification Service"
    )

    parser.add_argument(
        "--channel",
        choices=["sms", "whatsapp"],
        required=True
    )

    parser.add_argument(
        "--phone",
        required=True,
        help="Recipient phone in E.164 format"
    )

    parser.add_argument(
        "--message",
        required=True
    )

    args = parser.parse_args()

    service = NotificationService()

    result = service.send(
        phone=args.phone,
        message=args.message,
        channel=args.channel
    )

    print(result)
