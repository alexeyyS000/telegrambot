# flake8: noqa: F811
from aiogram import types
from bot.variable import dp
from .keyboards import actions_keyboard, pagination_keyboard
from db.dal.user import UserDAL
from db.client import session_maker


def get_id(callback_query_data):
    id = int(callback_query_data.split("#")[1])
    return id


def get_page(callback_query_data):
    page = int(callback_query_data.split("#")[2])
    return page


@dp.callback_query_handler(lambda c: c.data.startswith("add"))
async def handler(callback_query: types.CallbackQuery):
    id = get_id(callback_query.data)
    UserDAL(session_maker).update_one({"pending": False, "subscriber": True}, id=id)
    await callback_query.answer(text=f"id {id} added")


@dp.callback_query_handler(lambda c: c.data.startswith("ban"))
async def handler(callback_query: types.CallbackQuery):
    id = get_id(callback_query.data)
    UserDAL(session_maker).update_one({"pending": False, "banned": True}, id=id)
    await callback_query.answer(text=f"id {id} banned")


@dp.callback_query_handler(lambda c: c.data.startswith("refusal"))
async def handler(callback_query: types.CallbackQuery):
    id = get_id(callback_query.data)
    UserDAL(session_maker).delete_one(id=id)
    await callback_query.answer(text=f"id {id} refusal")


@dp.callback_query_handler(lambda c: c.data.startswith("make_admin"))
async def handler(callback_query: types.CallbackQuery):
    id = get_id(callback_query.data)
    UserDAL(session_maker).update_one({"admin": True}, id=id)
    await callback_query.answer(text=f"id {id} admin")


@dp.message_handler(lambda message: message.text == "/adminboard")
async def handler(message: types.Message):
    status = getattr(message.from_user, "user_instatce")
    if (status is not None) and (status.admin):
        data = UserDAL(session_maker).filter(pending=True).fetch(3)
        keyboard = pagination_keyboard(
            data["current_page"],
            data["prev_page"],
            data["next_page"],
            data["total_pages"],
            data["result"],
        )
        await message.answer(text="adminboard", reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data.startswith("page"))
async def handler(callback_query: types.CallbackQuery = None):
    page = callback_query.data.split("#")[1]
    data = UserDAL(session_maker).filter(pending=True).fetch(3, page)
    keyboard = pagination_keyboard(
        data["current_page"],
        data["prev_page"],
        data["next_page"],
        data["total_pages"],
        data["result"],
    )
    await callback_query.message.edit_reply_markup(reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data.startswith("id"))
async def handler(callback_query: types.CallbackQuery = None):
    id = get_id(callback_query.data)
    page = get_page(callback_query.data)
    await callback_query.message.edit_reply_markup(
        reply_markup=actions_keyboard(id, page)
    )
