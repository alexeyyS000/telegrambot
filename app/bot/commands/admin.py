# flake8: noqa: F811
from aiogram import types
from bot.variable import dp
from .keyboards import actions_keyboard, pagination_keyboard
from db.dal.user import UserDAL
from db.client import session_maker
from app.services.user import UserService
from .check_user_rights import check_admin


def get_id(callback_query_data):
    id = int(callback_query_data.split("#")[1])
    return id


def get_page(callback_query_data):
    page = int(callback_query_data.split("#")[2])
    return page


@dp.callback_query_handler(lambda c: c.data.startswith("add"))
async def handler(callback_query: types.CallbackQuery):
    id = get_id(callback_query.data)
    try:
        UserService(id).add()
        await callback_query.answer(text=f"id {id} added")
    except Exception:
        await callback_query.answer(text=f"id {id} already added")


@dp.callback_query_handler(lambda c: c.data.startswith("ban"))
async def handler(callback_query: types.CallbackQuery):
    id = get_id(callback_query.data)
    try:
        UserService(id).ban()
        await callback_query.answer(text=f"id {id} banned")
    except Exception:
        await callback_query.answer(text=f"id {id} already banned")


@dp.callback_query_handler(lambda c: c.data.startswith("refusal"))
async def handler(callback_query: types.CallbackQuery):
    id = get_id(callback_query.data)
    try:
        UserService(id).refusal()
        await callback_query.answer(text=f"id {id} refusaled")
    except Exception:
        await callback_query.answer(
            text=f"id {id} already refusaled"
        )  # тоже не знаю как избедать дублирования кода тут


@dp.callback_query_handler(lambda c: c.data.startswith("make_admin"))
async def handler(callback_query: types.CallbackQuery):
    id = get_id(callback_query.data)
    try:
        UserService(id).make_admin()
        await callback_query.answer(text=f"id {id} admin")
    except Exception:
        await callback_query.answer(text=f"id {id} already admin")


@dp.message_handler(lambda message: message.text == "/adminboard")
@check_admin
async def handler(message: types.Message):
    data = UserDAL(session_maker).fetch(3)
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
    data = UserDAL(session_maker).fetch(3, page)
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
