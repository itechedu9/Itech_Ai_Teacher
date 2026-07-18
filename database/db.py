import psycopg2


DB_NAME = "itech_ai_teacher"
DB_USER = "postgres"
DB_PASSWORD = "itech"
DB_HOST = "localhost"
DB_PORT = "5432"


def get_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
