
import re
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum


class Status(str, Enum):
    PENDING = "PENDING_VERIFICATION"
    REVIEW = "MANUAL_REVIEW"
    VERIFIED = "DOCUMENT_VERIFIED"
    ERROR = "INVALID_REQUEST"


@dataclass
class MexicanUser:
    first_name: str
    last_name: str
    curp: str
    consent: bool
    certificate_folio: str


def validate_curp(curp):
    """Format validation, not RENAPO verification."""
    pattern = (
        r"^[A-Z][AEIOUX][A-Z]{2}"
        r"\d{2}(0[1-9]|1[0-2])"
        r"(0[1-9]|[12]\d|3[01])"
        r"[HM]"
        r"(AS|BC|BS|CC|CL|CM|CS|CH|DF|"
        r"DG|GT|GR|HG|JC|MC|MN|MS|NT|"
        r"NL|OC|PL|QT|QR|SP|SL|SR|TC|"
        r"TS|TL|VZ|YN|ZS|NE)"
        r"[B-DF-HJ-NP-TV-Z]{3}"
        r"[A-Z0-9]\d$"
    )
    return bool(re.fullmatch(pattern, curp.upper()))


def create_verification(user):
    if not user.consent:
        return {
            "status": Status.ERROR.value,
            "reason": "Consent required"
        }

    if not validate_curp(user.curp):
        return {
            "status": Status.ERROR.value,
            "reason": "Invalid CURP format"
        }

    if not user.certificate_folio.strip():
        return {
            "status": Status.ERROR.value,
            "reason": "Certificate folio required"
        }

    return {
        "verification_id": str(uuid.uuid4()),
        "certificate_folio": user.certificate_folio,
        "status": Status.PENDING.value,
        "created_at": datetime.now(
            timezone.utc
        ).isoformat()
    }


def review_certificate(
    verification,
    authentic,
    identity_matches,
    reviewer_id
):
    """
    Call only after authorized verification
    against the issuing authority.

    authentic and identity_matches must be
    supplied by a trusted review process.
    """

    if not reviewer_id:
        raise ValueError("Reviewer ID required")

    if authentic is True and identity_matches is True:
        status = Status.VERIFIED.value
    else:
        status = Status.REVIEW.value

    verification["status"] = status
    verification["reviewer_id"] = reviewer_id

    # Document verification is NOT a finding
    # that the person has no criminal record.
    return verification


if __name__ == "__main__":
    user = MexicanUser(
        first_name="Juan",
        last_name="Perez",
        curp="PEPJ900515HJCRRN09",
        consent=True,
        certificate_folio="TEST-FOLIO-001"
    )

    result = create_verification(user)
    print(result)

    # Example only: do not use hardcoded
    # verification results in production.
