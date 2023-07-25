import locale
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton, ReplyKeyboardBuilder, KeyboardButton


def base_reply_markup():
    markup = ReplyKeyboardBuilder()
    markup.row(KeyboardButton(text="Кнопка 1"))
    markup.add(KeyboardButton(text="Кнопка 1"))
    return markup.as_markup(resize_keyboard=True)
