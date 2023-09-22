# flake8: noqa: F811
import datetime
from aiogram import types
from aiogram.dispatcher import FSMContext
from bot.variable import dp
from .keyboards import user_keyboard_unsubscribe
from bot.states import ClientState
from app.services.user import UserService
from .check_user_rights import check_registrated_user


async def chanel(message: types.Message, state: FSMContext):
    if message.text == "unsubscribe(cancel application)":
        return state.reset_state()


@dp.message_handler(text="/start")
@check_registrated_user
async def echo_send(message: types.Message, state: FSMContext):
    await message.answer(
        text="inter enter your full name", reply_markup=user_keyboard_unsubscribe()
    )

    await state.set_state(ClientState.start)


@dp.message_handler(state=ClientState.start)
async def echo_send(message: types.Message, state: FSMContext):
    if message.text == "unsubscribe(cancel application)":
        await state.reset_state()
    elif len(message.text.split()) != 3:
        await message.answer(text="incorrect try again")
        await state.set_state(ClientState.start)
    else:
        await message.answer(text="Enter your date of birth in the format DD/MM/YYYY")
        await state.update_data(name=message.text)
        await state.set_state(ClientState.full_name)


@dp.message_handler(state=ClientState.full_name)
async def echo_send(message: types.Message, state: FSMContext):
    if (
        message.text == "unsubscribe(cancel application)"
    ):  # пока не знаю как отдельной функцией
        await state.reset_state()
        return 1
    try:
        date_of_birth = datetime.datetime.strptime(message.text, "%d/%m/%Y")
    except:
        await message.answer(text="incorrect try again")
        await state.set_state(ClientState.full_name)
        return 1  # насколько адекватно пользоваться return в async
    await message.answer(text="registration completed wait")
    await state.update_data(date=date_of_birth)
    user_data = await state.get_data()
    user_model = {
        "birth_date": user_data["date"],
        "full_name": user_data["name"],
        "pending": True,
    }
    UserService(message.from_user.id).create(**user_model)
    await state.set_state(ClientState.birth_date)


@dp.message_handler(text="/start", state=ClientState.birth_date)
async def echo_send(message: types.Message):
    await message.answer(
        text="unsubscribe(cancel application)", reply_markup=user_keyboard_unsubscribe()
    )


@dp.message_handler(
    text="unsubscribe(cancel application)", state=ClientState.birth_date
)
async def echo_send(message: types.Message, state: FSMContext):
    UserService(message.from_user.id).refusal()
    await state.reset_state()
    await message.answer(text="done")
