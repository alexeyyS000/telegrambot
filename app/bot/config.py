from pydantic import BaseSettings
from aiogram import Bot, Dispatcher


class AdminSettings(BaseSettings):
    bot_token: str
    admin_id: int

    class Config:
        env_file = (".env", ".env.local")


bot = Bot(token=AdminSettings().bot_token)

dp = Dispatcher(bot)
