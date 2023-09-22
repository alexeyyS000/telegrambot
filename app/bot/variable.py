from aiogram import Bot, Dispatcher
from .config import AdminSettings
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token=AdminSettings().bot_token)

dp = Dispatcher(bot, storage=storage)
