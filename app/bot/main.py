from aiogram import executor
from commands import dp
from middleware import AuthorizationMiddleware


dp.middleware.setup(AuthorizationMiddleware())
executor.start_polling(dp, skip_updates=True)
