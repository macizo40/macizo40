"""
Collection of useful regular expression (regex) patterns in Python.
Each pattern is compiled for reuse.
"""

import re

# =========================
# BASIC PATTERNS
# =========================

WHITESPACE = re.compile(r"\s+")
NON_WHITESPACE = re.compile(r"\S+")
DIGITS = re.compile(r"\d+")
NON_DIGITS = re.compile(r"\D+")
WORD = re.compile(r"\w+")
NON_WORD = re.compile(r"\W+")

# =========================
# EMAIL / URL
# =========================

EMAIL = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
URL = re.compile(r"https?://(?:www\.)?[\w\-]+(?:\.[\w\-]+)+[/#?]?.*$")

# =========================
# PHONE NUMBERS
# =========================

PHONE_SIMPLE = re.compile(r"\+?\d{10,15}")
PHONE_FORMATTED = re.compile(r"\+?\d{1,3}?[-.\s]?\(?\d{1,4}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}")

# =========================
# DATES / TIMES
# =========================

DATE_YYYY_MM_DD = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
DATE_DD_MM_YYYY = re.compile(r"\b\d{2}/\d{2}/\d{4}\b")
TIME_24H = re.compile(r"\b([01]?\d|2[0-3]):[0-5]\d\b")

# =========================
# IP ADDRESSES
# =========================

IPV4 = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
IPV6 = re.compile(r"\b(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}\b")

# =========================
# NUMBERS
# =========================

INTEGER = re.compile(r"^-?\d+$")
FLOAT = re.compile(r"^-?\d*\.\d+$")

# =========================
# STRINGS
# =========================

QUOTED_STRING = re.compile(r'".*?"|\'.*?\'')
HTML_TAG = re.compile(r"<[^>]+>")

# =========================
# PASSWORD STRENGTH
# =========================

STRONG_PASSWORD = re.compile(
    r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
)

# =========================
# UUID
# =========================

UUID = re.compile(r"\b[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}\b")

# =========================
# HEX COLORS
# =========================

HEX_COLOR = re.compile(r"#(?:[0-9a-fA-F]{3}){1,2}\b")

# =========================
# CREDIT CARD (basic check)
# =========================

CREDIT_CARD = re.compile(r"\b(?:\d[ -]*?){13,16}\b")

# =========================
# USERNAME
# =========================

USERNAME = re.compile(r"^[a-zA-Z0-9._-]{3,20}$")

# =========================
# FILE PATHS
# =========================

UNIX_PATH = re.compile(r"(/[^/ ]*)+/?")
WINDOWS_PATH = re.compile(r"[a-zA-Z]:\\(?:[^\\/:*?\"<>|\r\n]+\\)*")

# =========================
# JSON KEY/VALUE (simple)
# =========================

JSON_KEY_VALUE = re.compile(r'"(.*?)"\s*:\s*"(.*?)"')

# =========================
# LOG PATTERNS (DevOps/SRE useful)
# =========================

LOG_LEVEL = re.compile(r"\b(INFO|DEBUG|ERROR|WARN|TRACE|FATAL)\b")
TIMESTAMP = re.compile(r"\b\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}:\d{2}\b")

# =========================
# SQL INJECTION (basic detection)
# =========================

SQL_INJECTION = re.compile(r"('.*--|;|--|\b(OR|AND)\b.+\=)", re.IGNORECASE)

# =========================
# HTML ENTITIES
# =========================

HTML_ENTITY = re.compile(r"&[a-zA-Z]+;")

# =========================
# USAGE EXAMPLES
# =========================

if __name__ == "__main__":
    test_email = "test@example.com"
    print("Valid email:", bool(EMAIL.match(test_email)))

    test_ip = "192.168.1.1"
    print("Valid IPv4:", bool(IPV4.match(test_ip)))

    test_password = "StrongP@ss1"
    print("Strong password:", bool(STRONG_PASSWORD.match(test_password)))
