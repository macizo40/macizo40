import psycopg2
import re

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "postgres",
    "user": "audit_user",
    "password": "CHANGE_ME"
}

# Possible PAN: 13-19 digits, optionally containing spaces/hyphens
PAN_PATTERN = re.compile(r"(?<!\d)(?:\d[ -]?){13,19}(?!\d)")


def luhn_check(number):
    """Validate a possible card number using the Luhn algorithm."""

    digits = [int(x) for x in number if x.isdigit()]

    if not 13 <= len(digits) <= 19:
        return False

    checksum = 0
    parity = len(digits) % 2

    for i, digit in enumerate(digits):
        if i % 2 == parity:
            digit *= 2

            if digit > 9:
                digit -= 9

        checksum += digit

    return checksum % 10 == 0


def mask_pan(number):
    """Never expose the complete PAN."""

    digits = "".join(c for c in number if c.isdigit())

    if len(digits) < 10:
        return "INVALID"

    return digits[:6] + "*" * (len(digits) - 10) + digits[-4:]


def get_databases(connection):
    cursor = connection.cursor()

    cursor.execute("""
        SELECT datname
        FROM pg_database
        WHERE datistemplate = false
        AND datallowconn = true
    """)

    databases = [row[0] for row in cursor.fetchall()]
    cursor.close()

    return databases


def get_text_columns(connection):
    cursor = connection.cursor()

    cursor.execute("""
        SELECT table_schema,
               table_name,
               column_name
        FROM information_schema.columns
        WHERE data_type IN (
            'character varying',
            'character',
            'text'
        )
        AND table_schema NOT IN (
            'pg_catalog',
            'information_schema'
        )
    """)

    columns = cursor.fetchall()
    cursor.close()

    return columns


def scan_column(connection, database, schema, table, column):
    cursor = connection.cursor()

    # PostgreSQL identifiers are quoted because metadata determines
    # the table/column names, not user input.
    query = f'''
        SELECT "{column}"
        FROM "{schema}"."{table}"
        WHERE "{column}" IS NOT NULL
    '''

    try:
        cursor.execute(query)

        for row in cursor:

            value = str(row[0])

            for candidate in PAN_PATTERN.findall(value):

                digits = re.sub(r"\D", "", candidate)

                if luhn_check(digits):

                    print(
                        f"[PAN FOUND] "
                        f"DB={database} "
                        f"TABLE={schema}.{table} "
                        f"COLUMN={column} "
                        f"PAN={mask_pan(digits)}"
                    )

    except Exception as error:
        connection.rollback()

        print(
            f"[SKIPPED] {database}.{schema}.{table}.{column}: "
            f"{error}"
        )

    finally:
        cursor.close()


def scan_database(database):

    config = DB_CONFIG.copy()
    config["dbname"] = database

    try:
        connection = psycopg2.connect(**config)

        print(f"\nScanning database: {database}")

        columns = get_text_columns(connection)

        for schema, table, column in columns:

            print(
                f"Checking "
                f"{schema}.{table}.{column}"
            )

            scan_column(
                connection,
                database,
                schema,
                table,
                column
            )

        connection.close()

    except Exception as error:
        print(f"Cannot scan database {database}: {error}")


def main():

    connection = psycopg2.connect(**DB_CONFIG)

    databases = get_databases(connection)

    connection.close()

    print("Databases discovered:")
    for database in databases:
        print(f"  - {database}")

    print("\nStarting PAN discovery scan...")

    for database in databases:
        scan_database(database)

    print("\nScan completed.")


if __name__ == "__main__":
    main()