from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

from middlewares.manage_users import ManageUserMiddleware

from handlers import routers

import database
import locale
import utils

from data.config import Telegram, WebHooks, Settings

from loguru import logger


locale.setlocale(locale.LC_ALL, '{}.UTF-8'.format(Settings.currency))


async def on_startup(bot: Bot, dispatcher: Dispatcher):
    # Setup utils
    utils.utils_setup(dispatcher.workflow_data)

    logger.info('[!] Bot is starting...')

    # Run database
    await database.load_database()
    logger.info('[3] Database loaded')

    # Register middlewares
    dispatcher.message.outer_middleware(ManageUserMiddleware())
    dispatcher.callback_query.outer_middleware(ManageUserMiddleware())
    logger.info('[2] Middlewares initialized')

    # Register routers
    dispatcher.include_router(router=routers.admin_router)
    dispatcher.include_router(router=routers.user_router)
    logger.info('[1] Routers included')

    # Register webhook
    await bot.set_webhook(f'{WebHooks.base_url}{WebHooks.bot_path}')

    # Logging info
    logger.info(f'[!] Bot started: @{(await bot.get_me()).username}!')


if __name__ == '__main__':
    session = AiohttpSession()
    bot = Bot(token=Telegram.token, session=session, parse_mode='HTML')

    storage = MemoryStorage()
    dp = Dispatcher(storage=storage, bot=bot)
    dp.startup.register(on_startup)

    application = web.Application()
    application['bot'] = bot
    application['dp'] = dp

    SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
    ).register(application, path=WebHooks.bot_path)

    setup_application(application, dp, bot=bot)
    web.run_app(application, host=WebHooks.listen_address, port=WebHooks.listen_port)
