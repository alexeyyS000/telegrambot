from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware
from app.services.user import UserService


class AuthorizationMiddleware(BaseMiddleware):
    async def on_process_message(self, message: types.Message, data: dict):
        user = UserService(message.from_user.id).instance
        data["user"] = user
