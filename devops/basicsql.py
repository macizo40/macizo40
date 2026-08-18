import psycopg2
from psycopg2.extras import RealDictCursor


class SQLQueryRunner:

    def __init__(self, host, port, database, user, password):
        self.connection = psycopg2.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password
        )

    def execute_query(self, query, parameters=None):
        """
        Execute a SELECT query using parameters.

        Example:
            query = '''
                SELECT *
                FROM users
                WHERE id = %s
                AND status = %s
            '''

            parameters = (100, "ACTIVE")
        """

        try:
            with self.connection.cursor(
                cursor_factory=RealDictCursor
            ) as cursor:

                cursor.execute(query, parameters or ())

                return cursor.fetchall()

        except Exception as e:
            print(f"SQL Error: {e}")
            return None

    def execute_update(self, query, parameters=None):
        """
        Execute INSERT, UPDATE or DELETE.
        """

        try:
            with self.connection.cursor() as cursor:

                cursor.execute(query, parameters or ())

                self.connection.commit()

                return cursor.rowcount

        except Exception as e:
            self.connection.rollback()
            print(f"SQL Error: {e}")
            return 0

    def close(self):
        self.connection.close()


# --------------------------------------------------
# Example
# --------------------------------------------------

if __name__ == "__main__":

    db = SQLQueryRunner(
        host="localhost",
        port=5432,
        database="mydatabase",
        user="myuser",
        password="mypassword"
    )

    # SQL with parameters
    query = """
        SELECT id, name, email
        FROM users
        WHERE status = %s
        AND age >= %s
    """

    parameters = (
        "ACTIVE",
        18
    )

    results = db.execute_query(query, parameters)

    for row in results:
        print(row)

    db.close()