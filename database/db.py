import psycopg2
import secrets
import datetime


def connect_sql():
    global conn, cur
    conn = psycopg2.connect("""
    host=localhost
    port=5432
    dbname=postgres
    user=postgres
    """)

    cur = conn.cursor()

    if conn:
        print('Database succesfully connected!')

    # cur.execute("DROP TABLE IF EXISTS user")

    cur.execute(
        "CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name VARCHAR, login VARCHAR);")
    conn.commit()


def show_users():
    cur.execute("SELECT * FROM users")
    return cur.fetchall()


async def insert_user(data):
    cur.execute(
        'INSERT INTO users (name, login) VALUES (%s, %s)',
        (data['name'], data['login']))
    cur.execute('SELECT LASTVAL()')
    lastid = cur.fetchone()[0]

    conn.commit()
    return lastid


def main():
    connect_sql()
    print(show_users())


if __name__ == '__main__':
    main()
