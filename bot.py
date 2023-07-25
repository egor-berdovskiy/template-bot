from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

from database import load_database

from data.config import Telegram, WebHooks

from loguru import logger


async def on_startup():
    logger.info('[!] Bot is starting...')
    # Run database
    await load_database()


async def on_shutdown():
    pass


if __name__ == '__main__':
    session = AiohttpSession()
    bot = Bot(token=Telegram.token, session=session, parse_mode='HTML')

    storage = MemoryStorage()
    dp = Dispatcher(storage=storage, bot=bot)
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    application = web.Application()
    application['bot'] = bot
    application['dp'] = dp

    SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
    ).register(application, host=WebHooks.bot_path)

    setup_application(application, dp, bot)
    web.run_app(application, host=WebHooks.listen_address, port=WebHooks.listen_port)
