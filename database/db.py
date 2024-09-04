import asyncpg
import secrets
import datetime

dbCredentials = {
    'host': '28efd-rw.db.pub.dbaas.postgrespro.ru',
    'port': '5432',
    'database': 'dbstud',
    'user': 'your_username',
    'password': 'your_password'
}


class Database:
    def __init__(self):
        self.pool = None

    async def connect(self):
        self.pool = await asyncpg.create_pool(**dbCredentials)

        query = "CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name VARCHAR, phone_number VARCHAR)"
        async with self.pool.acquire() as connection:
            await connection.execute(query)
        print('Успешное подключение')

    async def disconnect(self):
        await self.pool.close()

    async def fetch_users(self):
        query = "SELECT * FROM users"
        async with self.pool.acquire() as connection:
            return await connection.fetchall(query)

    async def insert_user(self, name: str, phone_number: str):
        query = "INSERT INTO users (name, phone_number) VALUES ($1, $2) RETURNING id"
        async with self.pool.acquire() as connection:
            user_id = await connection.fetchval(query, name, phone_number)
            return user_id


async def main():
    db = Database()
    await db.connect()
    users = await db.fetch_users()
    print(users)
    await db.disconnect()


if __name__ == '__main__':
    main()
