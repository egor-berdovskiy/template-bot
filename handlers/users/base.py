import locale

from aiogram import Bot, F, html
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from data.config import Settings
from helpers.keyboards.markups import base_reply_markup
from typing import Union

from ..routers import user_router


@user_router.message(Command(commands=['start']))
async def start(message: Message, state: FSMContext, user):
    await state.clear()

    await message.answer('🤖')
    await message.answer(
        f'Привет, {user.username}!\n'
        'Мы рады тебя видеть!',
        reply_markup=base_reply_markup()
    )