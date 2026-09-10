from dataclasses import dataclass
from datetime import date, datetime
import re
import unicodedata


@dataclass
class KYCApplicant:
    full_name: str
    date_of_birth: str       # YYYY-MM-DD
    country: str
    document_type: str
    document_number: str
    email: str
    phone: str


@dataclass
class KYCResult:
    approved: bool
    risk_level: str
    score: int
    reasons: list[str]


SUPPORTED_DOCUMENTS = {
    "MX": {"INE", "PASSPORT"},
    "US": {"PASSPORT", "DRIVER_LICENSE"},
    "CA": {"PASSPORT", "DRIVER_LICENSE"},
}


HIGH_RISK_COUNTRIES = {
    # Example placeholders only.
    # In production, obtain this information from a maintained compliance source.
    "XX",
    "YY",
}


def normalize_text(value: str) -> str:
    value = value.strip()
    value = unicodedata.normalize("NFKC", value)
    return re.sub(r"\s+", " ", value)


def calculate_age(date_of_birth: str) -> int:
    dob = datetime.strptime(date_of_birth, "%Y-%m-%d").date()
    today = date.today()

    age = today.year - dob.year

    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1

    return age


def valid_email(email: str) -> bool:
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return bool(re.match(pattern, email))


def valid_phone(phone: str) -> bool:
    cleaned = re.sub(r"[^\d+]", "", phone)
    return bool(re.match(r"^\+?\d{10,15}$", cleaned))


def valid_document_number(document_number: str) -> bool:
    cleaned = re.sub(r"[^A-Za-z0-9]", "", document_number)

    # Generic sanity check.
    # Replace this with country/document-specific validation.
    return 6 <= len(cleaned) <= 20


def run_quick_kyc(applicant: KYCApplicant) -> KYCResult:
    reasons = []
    risk_score = 0

    applicant.full_name = normalize_text(applicant.full_name)
    applicant.country = applicant.country.upper().strip()
    applicant.document_type = applicant.document_type.upper().strip()
    applicant.document_number = applicant.document_number.upper().strip()
    applicant.email = applicant.email.lower().strip()
    applicant.phone = applicant.phone.strip()

    # 1. Name validation
    if len(applicant.full_name.split()) < 2:
        reasons.append("Full legal name appears incomplete.")
        risk_score += 30

    # 2. Age validation
    try:
        age = calculate_age(applicant.date_of_birth)

        if age < 18:
            reasons.append("Applicant is under 18.")
            risk_score += 100

        elif age > 110:
            reasons.append("Date of birth appears invalid.")
            risk_score += 80

    except ValueError:
        reasons.append("Invalid date of birth format.")
        risk_score += 100

    # 3. Email validation
    if not valid_email(applicant.email):
        reasons.append("Invalid email address.")
        risk_score += 20

    # 4. Phone validation
    if not valid_phone(applicant.phone):
        reasons.append("Invalid phone number.")
        risk_score += 20

    # 5. Document validation
    if not valid_document_number(applicant.document_number):
        reasons.append("Document number format appears invalid.")
        risk_score += 40

    # 6. Country/document compatibility
    allowed_documents = SUPPORTED_DOCUMENTS.get(applicant.country)

    if allowed_documents is None:
        reasons.append("Country requires manual review.")
        risk_score += 30

    elif applicant.document_type not in allowed_documents:
        reasons.append(
            f"{applicant.document_type} is not supported for "
            f"{applicant.country}."
        )
        risk_score += 40

    # 7. Simplified country-risk check
    if applicant.country in HIGH_RISK_COUNTRIES:
        reasons.append("Country requires enhanced due diligence.")
        risk_score += 60

    # Determine result
    if risk_score >= 80:
        risk_level = "HIGH"
        approved = False

    elif risk_score >= 30:
        risk_level = "MEDIUM"
        approved = False

    else:
        risk_level = "LOW"
        approved = True

    if not reasons:
        reasons.append("Basic KYC checks passed.")

    return KYCResult(
        approved=approved,
        risk_level=risk_level,
        score=risk_score,
        reasons=reasons,
    )


if __name__ == "__main__":

    applicant = KYCApplicant(
        full_name="Juan Carlos Perez",
        date_of_birth="1990-05-15",
        country="MX",
        document_type="INE",
        document_number="ABC123456789",
        email="juan.perez@example.com",
        phone="+5213312345678",
    )

    result = run_quick_kyc(applicant)

    print("\n--- QUICK KYC RESULT ---")
    print(f"Applicant:   {applicant.full_name}")
    print(f"Approved:    {result.approved}")
    print(f"Risk Level:  {result.risk_level}")
    print(f"Risk Score:  {result.score}")

    print("\nChecks:")
    for reason in result.reasons:
        print(f"- {reason}")