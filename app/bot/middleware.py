from aiogram import BaseMiddleware
from services.user import get_user_service
from aiogram.types import Message
from typing import Callable, Dict, Any, Awaitable


class WeekendCallbackMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        with get_user_service(event.from_user.id) as user:
            user = user.instance
        data["user"] = user
        return await handler(event, data)
