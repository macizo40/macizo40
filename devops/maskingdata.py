import os
import hashlib
from typing import Optional

import psycopg2
from psycopg2.extras import execute_batch


# ---------------------------------------------------------
# Database configuration
# ---------------------------------------------------------

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", "5432")),
    "database": os.getenv("DB_NAME", "mydatabase"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD"),
}


# ---------------------------------------------------------
# Masking functions
# ---------------------------------------------------------

def mask_email(email: Optional[str]) -> Optional[str]:
    """
    Example:
        john.smith@example.com
        -> jo*******@example.com
    """
    if not email or "@" not in email:
        return email

    username, domain = email.split("@", 1)

    if len(username) <= 2:
        masked_username = "*" * len(username)
    else:
        masked_username = username[:2] + "*" * (len(username) - 2)

    return f"{masked_username}@{domain}"


def mask_phone(phone: Optional[str]) -> Optional[str]:
    """
    Example:
        3312345678
        -> ******5678
    """
    if not phone:
        return phone

    if len(phone) <= 4:
        return "*" * len(phone)

    return "*" * (len(phone) - 4) + phone[-4:]


def mask_name(name: Optional[str]) -> Optional[str]:
    """
    Example:
        Dainer
        -> D*****
    """
    if not name:
        return name

    if len(name) == 1:
        return "*"

    return name[0] + "*" * (len(name) - 1)


def mask_card(card_number: Optional[str]) -> Optional[str]:
    """
    Example:
        4111111111111111
        -> ************1111
    """
    if not card_number:
        return card_number

    if len(card_number) <= 4:
        return "*" * len(card_number)

    return "*" * (len(card_number) - 4) + card_number[-4:]


def pseudonymize(value: Optional[str]) -> Optional[str]:
    """
    Creates a deterministic SHA-256 pseudonym.

    Useful when you need the same original value to always produce
    the same masked identifier.
    """
    if not value:
        return value

    return hashlib.sha256(value.encode("utf-8")).hexdigest()


# ---------------------------------------------------------
# Database masking
# ---------------------------------------------------------

def mask_customer_data(batch_size: int = 500):
    connection = None

    try:
        connection = psycopg2.connect(**DB_CONFIG)
        connection.autocommit = False

        with connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT
                    customer_id,
                    first_name,
                    last_name,
                    email,
                    phone,
                    credit_card
                FROM customers
                """
            )

            while True:
                rows = cursor.fetchmany(batch_size)

                if not rows:
                    break

                updates = []

                for row in rows:
                    (
                        customer_id,
                        first_name,
                        last_name,
                        email,
                        phone,
                        credit_card,
                    ) = row

                    updates.append(
                        (
                            mask_name(first_name),
                            mask_name(last_name),
                            mask_email(email),
                            mask_phone(phone),
                            mask_card(credit_card),
                            customer_id,
                        )
                    )

                execute_batch(
                    cursor,
                    """
                    UPDATE customers
                    SET
                        first_name = %s,
                        last_name = %s,
                        email = %s,
                        phone = %s,
                        credit_card = %s
                    WHERE customer_id = %s
                    """,
                    updates,
                    page_size=batch_size,
                )

                connection.commit()

                print(f"Masked {len(updates)} records.")

        print("Database masking completed successfully.")

    except Exception as exc:
        if connection:
            connection.rollback()

        print(f"Database masking failed: {exc}")
        raise

    finally:
        if connection:
            connection.close()


# ---------------------------------------------------------
# Main
# ---------------------------------------------------------

if __name__ == "__main__":

    if not DB_CONFIG["password"]:
        raise RuntimeError(
            "DB_PASSWORD environment variable must be configured."
        )

    mask_customer_data()