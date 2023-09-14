from aiogram import Bot, Dispatcher
from .config import AdminSettings

bot = Bot(token=AdminSettings().bot_token)

dp = Dispatcher(bot)
