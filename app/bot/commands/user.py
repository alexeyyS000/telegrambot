# flake8: noqa: F811
from aiogram import types
from config import dp
from .keyboards import user_keyboard_subscribe, user_keyboard_unsubscribe
from db.dal.user import UserDAL
from db.client import session_maker
from schemas import User


@dp.message_handler(text="/start")
async def echo_send(message: types.Message):
    await message.answer(
        text="subscribe to receive alerts",
        reply_markup=user_keyboard_subscribe,
    )


@dp.message_handler(text="subscribe(status)")
async def echo_send(message: types.Message):
    user = User(id=message.from_user.id, pending=True)
    result = UserDAL(session_maker).get_or_create(user.dict(), id=user.id)
    if result[1] is True:
        await message.answer(text=f"application accepted, id = {message.from_user.id}")
    if result[1] is False:
        if result[0].subscriber is True:
            await message.answer(
                text=f"you are subscriber, id = {message.from_user.id}",
                reply_markup=user_keyboard_unsubscribe,
            )
        else:
            await message.answer(
                text=f"id = {message.from_user.id} application is processed"
            )


@dp.message_handler(text="unsubscribe")
async def echo_send(message: types.Message):
    status = UserDAL(session_maker).get_one_or_none(id=message.from_user.id)
    if status is None:
        await message.answer(text=f"you are not subscriber id = {message.from_user.id}")
    else:
        UserDAL(session_maker).delete_one(id=message.from_user.id)
        await message.answer(text="done")
