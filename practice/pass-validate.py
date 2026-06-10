import re

def validate_password(password: str) -> bool:
    """
    Validate a password according to common banking/enterprise rules:
    - At least 10 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    - At least one special character
    - No spaces
    """
    pattern = (
        r"^(?=.*[a-z])"          # at least one lowercase letter
        r"(?=.*[A-Z])"           # at least one uppercase letter
        r"(?=.*\d)"             # at least one digit
        r"(?=.*[@$!%*?&^#()_+\-=\[\]{};':\"\\|,.<>\/])"  # special character
        r"[^\s]{10,}$"          # minimum 10 characters and no spaces
    )

    return bool(re.match(pattern, password))