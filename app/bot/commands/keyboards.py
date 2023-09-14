from aiogram.types import (
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from . import samples


def user_keyboard_subscribe():
    user_keyboard_subscribe = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True
    )
    user_keyboard_subscribe.add("subscribe(status)")
    return user_keyboard_subscribe


def user_keyboard_unsubscribe():
    user_keyboard_unsubscribe = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True
    )
    user_keyboard_unsubscribe.add("unsubscribe(cancel application)")
    return user_keyboard_unsubscribe


def actions_keyboard(id: str, page: str):
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(text="add", callback_data=samples.add.format(id)),
        InlineKeyboardButton(text="ban", callback_data=samples.ban.format(id)),
        InlineKeyboardButton(text="refusal", callback_data=samples.refusal.format(id)),
        InlineKeyboardButton(
            text="make_admin", callback_data=samples.make_admin.format(id)
        ),
        InlineKeyboardButton(text="⬅️", callback_data=samples.page.format(page)),
    )
    return markup


def pagination_keyboard(data: dict):
    buttons = []
    current_page = data["current_page"]
    for x in data["result"]:
        user_button = [
            InlineKeyboardButton(
                f"{x.name} id : {x.id}", callback_data=f"id#{x.id}#{current_page}"
            )
        ]
        buttons.append(user_button)

    bottom_buttons = []
    if data["current_page"] != 1:
        prevPage = data["prev_page"]
        bottom_buttons.append(
            InlineKeyboardButton("⬅️", callback_data=samples.page.format(prevPage))
        )
    else:
        bottom_buttons.append(InlineKeyboardButton("⛔️", callback_data="stop"))

    bottom_buttons.append(
        InlineKeyboardButton(
            f'{data["current_page"]}/{data["total_pages"]}', callback_data="all_list"
        )
    )

    if data["current_page"] == data["total_pages"]:
        bottom_buttons.append(InlineKeyboardButton("⛔️", callback_data="stop"))
    else:
        nextPage = data["next_page"]
        bottom_buttons.append(
            InlineKeyboardButton("➡️", callback_data=samples.refusal.format(nextPage))
        )

    buttons.append(bottom_buttons)

    keyboard = InlineKeyboardMarkup(row_width=1, inline_keyboard=buttons)

    return keyboard
