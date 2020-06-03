import os
import aiomysql
from aiohttp import web
from board import Region, Territory


async def create_db_pool(app):
    app['pool'] = await aiomysql.create_pool(
            host=os.environ.get('DB_HOST'),
            user=os.environ.get('DB_USER'),
            password=os.environ.get('DB_PASS'),
            db=os.environ.get('DB_NAME'),
            port=int(os.environ.get('DB_PORT')),
        )

app = web.Application()

app.on_startup.append(create_db_pool)

app.add_routes([
        web.get('/v0/get-region', Region.get),
        web.get('/v0/get-territory', Territory.get)
        ])

if __name__ == "__main__":
    web.run_app(app)
