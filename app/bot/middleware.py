from aiogram import BaseMiddleware
from services.user import UserService
from aiogram.types import Message
from typing import Callable, Dict, Any, Awaitable


class WeekendCallbackMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        user = UserService(event.from_user.id).instance
        data["user"] = user
        return await handler(event, data)
