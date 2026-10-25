import psycopg
import os
from dotenv import load_dotenv
import json

load_dotenv()

database_url=os.environ.get("DATABASE_URL")

def check_database_connection():
    with psycopg.connect(database_url) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT 1")
            return cur.fetchone()

def save_experiment(name: str, config: dict) -> int:
    with psycopg.connect(database_url) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO experiments (name, config)
                VALUES (%s, %s)
                RETURNING id
                """,
                (name, json.dumps(config)),
            )
            experiment_id = cur.fetchone()[0]
    return experiment_id

def get_experiment() -> list[dict]:
    with psycopg.connect(database_url) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM experiments")
            rows = cur.fetchall()
        return [
            {
                "id": row[0],
                "name": row[1],
                "config": row[2],
            }
            for row in rows
        ]