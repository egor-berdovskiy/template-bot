from aiogram.utils.keyboard import CallbackData


class TestCallback(CallbackData, prefix='test'):
    action: str
