from aiogram import Router, F
from filters.access_filter import AdminFilter


user_router = Router()
admin_router = Router()

admin_router.message.filter(AdminFilter())
admin_router.callback_query.filter(AdminFilter())

admin_router.message.filter(F.chat.type.in_(["private"]))
admin_router.callback_query.filter(F.message.chat.type.in_(["private"]))

user_router.message.filter(F.chat.type.in_(["private"]))
user_router.callback_query.filter(F.message.chat.type.in_(["private"]))
