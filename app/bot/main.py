from aiogram import executor
from commands import dp
from middleware import Middleware


dp.middleware.setup(Middleware())
executor.start_polling(dp, skip_updates=True)
