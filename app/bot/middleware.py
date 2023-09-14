from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware
from db.dal.user import UserDAL
from db.client import session_maker


class Middleware(BaseMiddleware):
    async def on_process_message(self, message: types.Message, data: dict):
        user = UserDAL(session_maker).get_one_or_none(id=message.from_user.id)
        setattr(message.from_user, "user_instatce", user)
