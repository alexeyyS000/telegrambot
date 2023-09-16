from aiogram import executor
from commands import dp
from middleware import AuthorizationMiddle


dp.middleware.setup(AuthorizationMiddle())
executor.start_polling(dp, skip_updates=True)
