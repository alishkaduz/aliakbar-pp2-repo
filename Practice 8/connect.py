import psycopg2
from config import DB_CONFIG


def get_connection():
    return psycopg2.connect(**DB_CONFIG)


def init_db():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS contacts (
                    id         SERIAL PRIMARY KEY,
                    username   VARCHAR(100) UNIQUE NOT NULL,
                    first_name VARCHAR(100),
                    last_name  VARCHAR(100),
                    phone      VARCHAR(30) NOT NULL
                );
            """)
            for filename in ("functions.sql", "procedures.sql"):
                with open(filename, "r") as f:
                    cur.execute(f.read())
        conn.commit()
    print("DB ready.")


if __name__ == "__main__":
    init_db()