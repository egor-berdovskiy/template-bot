from tortoise import Tortoise
from data.config import DataBase
from loguru import logger

connection_string = f'postgres://{DataBase.user}:{DataBase.password}@{DataBase.host}:{DataBase.port}/{DataBase.database}'
modules = {'models': ['database.models']}

async def load_database(*_, **__):
    await Tortoise.init(db_url=connection_string, modules=modules)
    await Tortoise.generate_schemas()
    