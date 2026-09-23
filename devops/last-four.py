import psycopg2
from psycopg2 import sql
import re

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "postgres",
    "user": "audit_user",
    "password": "CHANGE_ME"
}

# Exactly four digits
LAST4_PATTERN = re.compile(r"^\d{4}$")

# Column names that make a 4-digit value more likely to be card-related
CARD_COLUMN_KEYWORDS = [
    "last4",
    "last_4",
    "card_last",
    "card",
    "pan",
    "account_number",
    "payment"
]


def get_databases(connection):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT datname
            FROM pg_database
            WHERE datistemplate = false
              AND datallowconn = true
        """)

        return [row[0] for row in cursor.fetchall()]


def get_columns(connection):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT
                table_schema,
                table_name,
                column_name,
                data_type
            FROM information_schema.columns
            WHERE table_schema NOT IN (
                'pg_catalog',
                'information_schema'
            )
            AND data_type IN (
                'character varying',
                'character',
                'text',
                'smallint',
                'integer',
                'bigint'
            )
            ORDER BY
                table_schema,
                table_name,
                ordinal_position
        """)

        return cursor.fetchall()


def looks_card_related(column):
    column_lower = column.lower()

    return any(
        keyword in column_lower
        for keyword in CARD_COLUMN_KEYWORDS
    )


def scan_column(
    connection,
    database,
    schema,
    table,
    column
):
    query = sql.SQL("""
        SELECT {column}::text
        FROM {schema}.{table}
        WHERE {column} IS NOT NULL
    """).format(
        column=sql.Identifier(column),
        schema=sql.Identifier(schema),
        table=sql.Identifier(table)
    )

    try:
        with connection.cursor() as cursor:

            cursor.execute(query)

            for row in cursor:

                value = str(row[0]).strip()

                if LAST4_PATTERN.fullmatch(value):

                    priority = (
                        "HIGH"
                        if looks_card_related(column)
                        else "REVIEW"
                    )

                    print(
                        f"[{priority}] "
                        f"DB={database} "
                        f"TABLE={schema}.{table} "
                        f"COLUMN={column} "
                        f"LAST4={value}"
                    )

    except Exception as error:

        connection.rollback()

        print(
            f"[SKIPPED] "
            f"{database}.{schema}.{table}.{column}: "
            f"{error}"
        )


def scan_database(database):

    config = DB_CONFIG.copy()
    config["dbname"] = database

    try:
        connection = psycopg2.connect(**config)

        print("=" * 70)
        print(f"Scanning database: {database}")
        print("=" * 70)

        columns = get_columns(connection)

        for schema, table, column, data_type in columns:

            print(
                f"Checking "
                f"{schema}.{table}.{column} "
                f"({data_type})"
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

        print(
            f"[ERROR] Cannot scan database "
            f"{database}: {error}"
        )


def main():

    try:
        connection = psycopg2.connect(**DB_CONFIG)

        databases = get_databases(connection)

        connection.close()

        print("\nDatabases discovered:")

        for database in databases:
            print(f"  - {database}")

        print("\nStarting LAST4 discovery scan...\n")

        for database in databases:
            scan_database(database)

        print("\nScan completed.")

    except Exception as error:

        print(f"Fatal error: {error}")


if __name__ == "__main__":
    main()