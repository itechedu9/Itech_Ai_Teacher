from database.db import get_connection

def login(username, password):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT id, username, role
        FROM users
        WHERE username=%s
        AND password_hash=%s
    """, (username, password))

    user = cur.fetchone()

    cur.close()
    conn.close()

    return user
