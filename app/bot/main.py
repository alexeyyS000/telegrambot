from aiogram import executor
from commands import dp


executor.start_polling(dp, skip_updates=True)
