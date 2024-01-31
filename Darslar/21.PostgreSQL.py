from asyncpg import create_pool
import asyncio
class PostgreSql:
    def __init__(self):
        self.pool = None
#
    async def create(self):
        self.pool = await create_pool(
            user = "postgres",
            password = "root",
            host = "localhost",
            database = "postgres"
        )
#
    async def execute(self, sql, fetch=False, fetchval=False, fetchrow=False, execute=False):
        async with self.pool.acquire() as connection:
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(sql)
                elif fetchval:
                    result = await connection.fetchval(sql)
                elif fetchrow:
                    result = await connection.fetchrow(sql)
                elif execute:
                    result = await connection.execute(sql)
            return result
#
    async def uquvchilar(self):
        sql = f"select * from uquvchilar"
        return await self.execute(sql, fetch=True)
#
#
async def test():
    db = PostgreSql()
    await db.create()
    users = await db.uquvchilar()
    print(users)
#
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(test())
