
import os
import re
import logging

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

load_dotenv()

app = FastAPI(title="Client OTP Service")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("otp_service")

ACCOUNT_SID = os.environ["TWILIO_ACCOUNT_SID"]
AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
SERVICE_SID = os.environ["TWILIO_VERIFY_SERVICE_SID"]

twilio_client = Client(ACCOUNT_SID, AUTH_TOKEN)


class OTPRequest(BaseModel):
    phone_number: str


class OTPVerification(BaseModel):
    phone_number: str
    otp_code: str


def validate_phone(phone: str):
    # International E.164 format
    if not re.fullmatch(r"\+[1-9]\d{7,14}", phone):
        raise HTTPException(
            status_code=400,
            detail="Invalid phone number. Use E.164 format."
        )
    return phone


@app.post("/send-otp")
def send_otp(request: OTPRequest):
    phone = validate_phone(request.phone_number)

    try:
        verification = (
            twilio_client.verify.v2
            .services(SERVICE_SID)
            .verifications.create(
                to=phone,
                channel="sms"
            )
        )

        return {
            "message": "OTP request processed",
            "status": verification.status
        }

    except TwilioRestException:
        logger.exception("OTP delivery provider error")
        raise HTTPException(
            status_code=502,
            detail="Unable to process OTP request"
        )


@app.post("/verify-otp")
def verify_otp(request: OTPVerification):
    phone = validate_phone(request.phone_number)

    if not re.fullmatch(r"\d{4,10}", request.otp_code):
        raise HTTPException(
            status_code=400,
            detail="Invalid OTP format"
        )

    try:
        result = (
            twilio_client.verify.v2
            .services(SERVICE_SID)
            .verification_checks.create(
                to=phone,
                code=request.otp_code
            )
        )

        if result.status == "approved":
            return {
                "verified": True,
                "message": "OTP verified successfully"
            }

        return {
            "verified": False,
            "message": "Invalid or expired OTP"
        }

    except TwilioRestException:
        logger.exception("OTP verification provider error")
        raise HTTPException(
            status_code=502,
            detail="Unable to verify OTP"
        )
