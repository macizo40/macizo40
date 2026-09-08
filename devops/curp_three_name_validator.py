#!/usr/bin/env python3
"""Validate CURP records with three separate identity-name components.

Expected CSV columns:
    curp,nombres,apellido_paterno,apellido_materno

The program creates valid and invalid CSV files without changing the input.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
import unicodedata
from datetime import date
from pathlib import Path


STATE_CODES = {
    "AS", "BC", "BS", "CC", "CL", "CM", "CS", "CH", "DF", "DG", "GT",
    "GR", "HG", "JC", "MC", "MN", "MS", "NT", "NL", "OC", "PL", "QT",
    "QR", "SP", "SL", "SR", "TC", "TS", "TL", "VZ", "YN", "ZS", "NE",
}
CURP_PATTERN = re.compile(
    r"^[A-Z][AEIOUX][A-Z]{2}"
    r"\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])"
    r"[HM](?:" + "|".join(sorted(STATE_CODES)) + r")"
    r"[B-DF-HJ-NP-TV-Z]{3}[A-Z0-9]\d$"
)
NAME_PATTERN = re.compile(r"^[A-ZÑ]+(?:[ '-][A-ZÑ]+)*$")
CHECKSUM_ALPHABET = "0123456789ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
REQUIRED_COLUMNS = ("curp", "nombres", "apellido_paterno", "apellido_materno")


def normalize(value: str | None) -> str:
    """Normalize whitespace/case while preserving Ñ."""
    text = unicodedata.normalize("NFC", value or "").strip().upper()
    return " ".join(text.split())


def valid_check_digit(curp: str) -> bool:
    """Validate the 18th CURP character using the official modulus routine."""
    if len(curp) != 18 or not curp[-1].isdigit():
        return False
    try:
        total = sum(CHECKSUM_ALPHABET.index(char) * (18 - index)
                    for index, char in enumerate(curp[:17]))
    except ValueError:
        return False
    expected = (10 - total % 10) % 10
    return int(curp[-1]) == expected


def valid_birth_date(curp: str) -> bool:
    """Validate YYMMDD, inferring century from the homoclave position."""
    try:
        year_two_digits = int(curp[4:6])
        # Position 17 is numeric for births before 2000 and alphabetic for 2000+.
        century = 1900 if curp[16].isdigit() else 2000
        date(century + year_two_digits, int(curp[6:8]), int(curp[8:10]))
        return True
    except (ValueError, IndexError):
        return False


def validate_record(row: dict[str, str]) -> list[str]:
    errors: list[str] = []
    curp = normalize(row.get("curp"))
    fields = {
        "nombres": normalize(row.get("nombres")),
        "apellido_paterno": normalize(row.get("apellido_paterno")),
        "apellido_materno": normalize(row.get("apellido_materno")),
    }

    missing = [field for field, value in fields.items() if not value]
    if missing:
        errors.append("Faltan los 3 componentes de nombre: " + ", ".join(missing))

    for field, value in fields.items():
        if value and not NAME_PATTERN.fullmatch(value):
            errors.append(f"{field} contiene caracteres no permitidos")

    if not CURP_PATTERN.fullmatch(curp):
        errors.append("CURP no tiene una estructura válida de 18 caracteres")
    else:
        if not valid_birth_date(curp):
            errors.append("La fecha de nacimiento contenida en la CURP no es válida")
        if not valid_check_digit(curp):
            errors.append("El dígito verificador de la CURP no es válido")

    return errors


def output_columns(input_columns: list[str]) -> list[str]:
    return input_columns + ["validation_status", "validation_errors"]


def process_csv(source: Path, valid_path: Path, invalid_path: Path) -> tuple[int, int]:
    valid_count = invalid_count = 0
    with source.open("r", newline="", encoding="utf-8-sig") as input_file:
        reader = csv.DictReader(input_file)
        if not reader.fieldnames:
            raise ValueError("El archivo CSV no contiene encabezados")

        original_headers = list(reader.fieldnames)
        canonical_headers = [normalize(header).lower() for header in original_headers]
        missing_columns = [name for name in REQUIRED_COLUMNS if name not in canonical_headers]
        if missing_columns:
            raise ValueError("Faltan columnas requeridas: " + ", ".join(missing_columns))

        header_map = dict(zip(original_headers, canonical_headers))
        result_headers = output_columns(original_headers)

        with (
            valid_path.open("w", newline="", encoding="utf-8") as valid_file,
            invalid_path.open("w", newline="", encoding="utf-8") as invalid_file,
        ):
            valid_writer = csv.DictWriter(valid_file, fieldnames=result_headers)
            invalid_writer = csv.DictWriter(invalid_file, fieldnames=result_headers)
            valid_writer.writeheader()
            invalid_writer.writeheader()

            for row in reader:
                canonical_row = {header_map[key]: value for key, value in row.items()}
                errors = validate_record(canonical_row)
                output_row = dict(row)
                output_row["validation_status"] = "INVALID" if errors else "VALID"
                output_row["validation_errors"] = " | ".join(errors)
                if errors:
                    invalid_writer.writerow(output_row)
                    invalid_count += 1
                else:
                    valid_writer.writerow(output_row)
                    valid_count += 1

    return valid_count, invalid_count


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate CURP users with nombres + two separate surnames."
    )
    parser.add_argument("csv_file", type=Path, help="Input CSV file")
    parser.add_argument("--valid-output", type=Path, default=Path("usuarios_validos.csv"))
    parser.add_argument("--invalid-output", type=Path, default=Path("usuarios_invalidos.csv"))
    args = parser.parse_args()

    try:
        valid_count, invalid_count = process_csv(
            args.csv_file, args.valid_output, args.invalid_output
        )
    except (OSError, UnicodeError, csv.Error, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    print(f"Usuarios válidos: {valid_count}")
    print(f"Usuarios inválidos: {invalid_count}")
    print(f"Archivo válido: {args.valid_output}")
    print(f"Archivo inválido: {args.invalid_output}")
    return 2 if invalid_count else 0


if __name__ == "__main__":
    raise SystemExit(main())
