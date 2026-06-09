import re

def is_valid_curp(curp):
    pattern = (
        r'^[A-Z][AEIOU][A-Z]{2}'   # First 4 letters
        r'\d{6}'                  # Birth date (YYMMDD)
        r'[HM]'                   # Gender
        r'(AS|BC|BS|CC|CL|CM|CS|CH|DF|DG|GT|GR|HG|JC|MC|MN|MS|NT|NL|OC|PL|QT|QR|SP|SL|SR|TC|TS|TL|VZ|YN|ZS|NE)'
        r'[B-DF-HJ-NP-TV-Z]{3}'   # Internal consonants
        r'[A-Z0-9]'               # Homoclave
        r'\d$'                    # Check digit
    )

    return bool(re.match(pattern, curp.upper()))


# Examples
curps = [
    "GODE561231HDFRRN09",
    "BADD110313HCMLNS09",
    "INVALIDCURP123456"
]

for curp in curps:
    print(f"{curp}: {is_valid_curp(curp)}")