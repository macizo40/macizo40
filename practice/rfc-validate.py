import re

def is_valid_rfc(rfc):
    """
    Validate Mexican RFC format.
    Supports individuals (13 chars) and companies (12 chars).
    """
    pattern = r'^([A-ZÑ&]{3,4})(\d{6})([A-Z0-9]{3})$'
    return bool(re.match(pattern, rfc.upper()))

# Examples
rfcs = [
    "XAXX010101000",   # Generic individual RFC
    "ABC8501011A2",   # Company RFC
    "COSC8001137NA",  # Individual RFC
    "INVALID123"
]

for rfc in rfcs:
    print(f"{rfc}: {is_valid_rfc(rfc)}")