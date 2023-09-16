# flake8: noqa: F811
from aiogram import types
from bot.variable import dp
from .keyboards import user_keyboard_subscribe, user_keyboard_unsubscribe
from db.dal.user import UserDAL
from db.client import session_maker


@dp.message_handler(text="/start")
async def echo_send(message: types.Message):
    await message.answer(
        text="subscribe to receive alerts",
        reply_markup=user_keyboard_subscribe(),
    )


@dp.message_handler(text="subscribe(status)")
async def echo_send(message: types.Message):
    status = getattr(message.from_user, "user_instatce")
    if status is None:
        user = {
            "id": message.from_user.id,
            "name": message.from_user.full_name,
            "pending": True,
        }
        UserDAL(session_maker).create_one(**user)
        await message.answer(
            text=f"application accepted, id = {message.from_user.id}",
            reply_markup=user_keyboard_unsubscribe(),
        )
    else:
        if status.subscriber:
            await message.answer(
                text=f"you are subscriber, id = {message.from_user.id}",
                reply_markup=user_keyboard_unsubscribe(),
            )
        else:
            await message.answer(
                text=f"id = {message.from_user.id} application is processed",
                reply_markup=user_keyboard_unsubscribe(),
            )


@dp.message_handler(text="unsubscribe(cancel application)")
async def echo_send(message: types.Message):
    status = getattr(message.from_user, "user_instatce")
    if status is None:
        await message.answer(text=f"you are not subscriber id = {message.from_user.id}")
    else:
        UserDAL(session_maker).delete_one(id=message.from_user.id)
        await message.answer(text="done")
