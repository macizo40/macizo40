"""
MDES-style tokenization example.

PURPOSE
-------
Demonstrates a production-style architecture for:

PAN
  -> encrypted digitization payload
  -> MDES client
  -> tokenization response
  -> payment token + Token Unique Reference (TUR)

IMPORTANT
---------
This sample does NOT generate a real Mastercard TUR.

A real TUR is returned by Mastercard MDES after successful
token provisioning.

Never hard-code production PANs, private keys, API credentials,
or encryption keys in source code.
"""

import os
import json
import uuid
import base64
import secrets
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional

import requests


# ============================================================
# Configuration
# ============================================================

MDES_BASE_URL = os.getenv(
    "MDES_BASE_URL",
    "https://sandbox.api.mastercard.com"
)

# Replace with the endpoint supplied in your MDES onboarding docs.
MDES_DIGITIZE_PATH = os.getenv(
    "MDES_DIGITIZE_PATH",
    "/mdes/digitization/v1/tokenize"
)

TOKEN_REQUESTOR_ID = os.getenv(
    "TOKEN_REQUESTOR_ID",
    "YOUR_TOKEN_REQUESTOR_ID"
)

API_KEY = os.getenv(
    "MDES_API_KEY",
    "sandbox-api-key"
)

USE_MOCK = os.getenv(
    "MDES_USE_MOCK",
    "true"
).lower() == "true"


# ============================================================
# Data models
# ============================================================

@dataclass
class CardData:
    pan: str
    expiry_month: str
    expiry_year: str
    cardholder_name: Optional[str] = None


@dataclass
class DeviceData:
    device_id: str
    device_type: str
    os_name: str


@dataclass
class TokenizationResult:
    request_id: str
    status: str
    token_unique_reference: Optional[str]
    payment_token: Optional[str]
    token_expiry_month: Optional[str]
    token_expiry_year: Optional[str]


# ============================================================
# Validation
# ============================================================

def luhn_valid(number: str) -> bool:
    digits = [int(c) for c in number if c.isdigit()]

    checksum = 0
    parity = len(digits) % 2

    for i, digit in enumerate(digits):
        if i % 2 == parity:
            digit *= 2

            if digit > 9:
                digit -= 9

        checksum += digit

    return checksum % 10 == 0


def validate_card(card: CardData) -> None:

    if not card.pan.isdigit():
        raise ValueError("PAN must contain digits only")

    if not 12 <= len(card.pan) <= 19:
        raise ValueError("Invalid PAN length")

    if not luhn_valid(card.pan):
        raise ValueError("PAN failed Luhn validation")

    month = int(card.expiry_month)

    if month < 1 or month > 12:
        raise ValueError("Invalid expiry month")


# ============================================================
# Sensitive payload
# ============================================================

def build_sensitive_card_payload(card: CardData) -> dict:

    return {
        "accountNumber": card.pan,
        "expiryMonth": card.expiry_month,
        "expiryYear": card.expiry_year,
        "cardholderName": card.cardholder_name,
    }


# ============================================================
# Encryption boundary
# ============================================================

def encrypt_for_mdes(payload: dict) -> str:
    """
    Placeholder encryption layer.

    In a real MDES implementation this function should implement
    the Mastercard-defined payload encryption mechanism from your
    onboarding documentation.

    Possible production techniques may involve:

      - JWE
      - RSA-OAEP
      - AES-GCM
      - Mastercard-issued certificates / keys

    DO NOT replace this with base64 in production.

    Base64 here is only used so this example can run.
    """

    raw_json = json.dumps(payload).encode("utf-8")

    return base64.b64encode(raw_json).decode("utf-8")


# ============================================================
# Digitization request
# ============================================================

def build_digitization_request(
    card: CardData,
    device: DeviceData
) -> dict:

    request_id = str(uuid.uuid4())

    sensitive_payload = build_sensitive_card_payload(card)

    encrypted_card_data = encrypt_for_mdes(
        sensitive_payload
    )

    return {
        "requestId": request_id,

        "tokenRequestorId": TOKEN_REQUESTOR_ID,

        "tokenType": "PAYMENT_TOKEN",

        "accountData": encrypted_card_data,

        "device": {
            "deviceId": device.device_id,
            "deviceType": device.device_type,
            "operatingSystem": device.os_name
        },

        "requestTimestamp": datetime.now(
            timezone.utc
        ).isoformat()
    }


# ============================================================
# HTTP authentication
# ============================================================

def create_headers() -> dict:
    """
    Simplified authentication.

    Actual Mastercard APIs frequently require authentication/
    signing mechanisms supplied during developer onboarding.

    Plug the Mastercard-supported signing mechanism here.
    """

    return {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }


# ============================================================
# MDES client
# ============================================================

class MDESClient:

    def __init__(self):
        self.base_url = MDES_BASE_URL

    def tokenize(
        self,
        card: CardData,
        device: DeviceData
    ) -> TokenizationResult:

        validate_card(card)

        request_payload = build_digitization_request(
            card,
            device
        )

        if USE_MOCK:
            return self._mock_tokenize(request_payload)

        return self._send_to_mdes(request_payload)

    def _send_to_mdes(
        self,
        payload: dict
    ) -> TokenizationResult:

        url = (
            self.base_url.rstrip("/")
            + MDES_DIGITIZE_PATH
        )

        response = requests.post(
            url,
            json=payload,
            headers=create_headers(),
            timeout=30
        )

        response.raise_for_status()

        data = response.json()

        return self._parse_response(
            payload["requestId"],
            data
        )

    def _parse_response(
        self,
        request_id: str,
        data: dict
    ) -> TokenizationResult:

        """
        Field mappings may need to be adjusted to match the
        MDES API version provisioned for your organization.
        """

        return TokenizationResult(
            request_id=request_id,

            status=data.get(
                "status",
                "UNKNOWN"
            ),

            token_unique_reference=data.get(
                "tokenUniqueReference"
            ),

            payment_token=data.get(
                "paymentToken"
            ),

            token_expiry_month=data.get(
                "tokenExpiryMonth"
            ),

            token_expiry_year=data.get(
                "tokenExpiryYear"
            )
        )

    # ========================================================
    # Mock MDES environment
    # ========================================================

    def _mock_tokenize(
        self,
        payload: dict
    ) -> TokenizationResult:

        """
        Simulates a successful MDES provisioning response.
        """

        fake_tur = (
            "TUR-"
            + secrets.token_hex(24).upper()
        )

        fake_token = (
            "5"
            + "".join(
                str(secrets.randbelow(10))
                for _ in range(15)
            )
        )

        return TokenizationResult(
            request_id=payload["requestId"],
            status="APPROVED",
            token_unique_reference=fake_tur,
            payment_token=fake_token,
            token_expiry_month="12",
            token_expiry_year="2031"
        )


# ============================================================
# Application
# ============================================================

def main():

    #
    # TEST PAN ONLY.
    #
    # Do not put real customer PANs in source code.
    #

    card = CardData(
        pan="5555555555554444",
        expiry_month="12",
        expiry_year="2030",
        cardholder_name="TEST USER"
    )

    device = DeviceData(
        device_id=str(uuid.uuid4()),
        device_type="ANDROID",
        os_name="Android"
    )

    client = MDESClient()

    try:

        result = client.tokenize(
            card,
            device
        )

        print("\nMDES TOKENIZATION RESULT")
        print("------------------------")

        print(
            "Request ID:",
            result.request_id
        )

        print(
            "Status:",
            result.status
        )

        print(
            "Payment Token:",
            result.payment_token
        )

        print(
            "Token Unique Reference:",
            result.token_unique_reference
        )

        print(
            "Token Expiration:",
            f"{result.token_expiry_month}/"
            f"{result.token_expiry_year}"
        )

    except requests.HTTPError as exc:

        print(
            "MDES HTTP error:",
            exc
        )

    except Exception as exc:

        print(
            "Tokenization error:",
            exc
        )


if __name__ == "__main__":
    main()