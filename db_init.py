import psycopg2
from config import DB_CONFIG

def init_db():
    conn = psycopg2.connect(**DB_CONFIG)

    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS companies (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        );
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS vacancies (
            id SERIAL PRIMARY KEY,
            company_id INTEGER REFERENCES companies(id),
            name VARCHAR(255) NOT NULL,
            salary INTEGER,
            currency VARCHAR(10),
            url VARCHAR(255)
        );
    """)
    conn.commit()
    cur.close()
    conn.close()
