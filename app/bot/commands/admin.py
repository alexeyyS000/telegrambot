# flake8: noqa: F811
from aiogram import types
from config import AdminSettings
from config import dp
from .keyboards import actions_keyboard, pagination_keyboard
from db.dal.user import UserDAL
from db.client import session_maker

admin_id = AdminSettings().admin_id


@dp.callback_query_handler(lambda c: c.data.startswith("add"))
async def handler(callback_query: types.CallbackQuery):
    id = int(callback_query.data.split("#")[1].split("_")[0])
    UserDAL(session_maker).update_one({"pending": False, "subscriber": True}, id=id)
    await callback_query.answer(text=f"id {id} added")


@dp.callback_query_handler(lambda c: c.data.startswith("ban"))
async def handler(callback_query: types.CallbackQuery):
    id = int(callback_query.data.split("#")[1].split("_")[0])
    UserDAL(session_maker).update_one({"pending": False, "banned": True}, id=id)
    await callback_query.answer(text=f"id {id} banned")


@dp.callback_query_handler(lambda c: c.data.startswith("refusal"))
async def handler(callback_query: types.CallbackQuery):
    id = int(callback_query.data.split("#")[1].split("_")[0])
    UserDAL(session_maker).update_one({"pending": False}, id=id)
    await callback_query.answer(text=f"id {id} refusal")


@dp.message_handler(lambda message: message.text == "/adminboard")
async def handler(message: types.Message):
    if message.from_user.id == admin_id:
        data = UserDAL(session_maker).filter(pending=True).fetch(3)
        keyboard = await pagination_keyboard(data)
        await message.answer(text="adminboard", reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data.startswith("page"))
async def handler(query: types.CallbackQuery = None):
    page = query.data.split("#")[1]
    data = UserDAL(session_maker).filter(pending=True).fetch(3, page)
    keyboard = await pagination_keyboard(data)
    await query.message.edit_reply_markup(reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data.startswith("id"))
async def handler(query: types.CallbackQuery = None):
    id = query.data.split("#")[1].split("_")[0]
    page = query.data.split("_")[1]
    await query.message.edit_reply_markup(reply_markup=actions_keyboard(id, page))
