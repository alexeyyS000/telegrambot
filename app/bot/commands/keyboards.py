from aiogram.types import (
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from . import samples


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


def pagination_keyboard(current_page, prev_page, next_page, total_pages, result):
    buttons = []
    current_page = current_page
    for x in result:
        user_button = [
            InlineKeyboardButton(
                f"{x.full_name} id : {x.id}", callback_data=f"id#{x.id}#{current_page}"
            )
        ]
        buttons.append(user_button)

    bottom_buttons = []
    if current_page != 1:
        prevPage = prev_page
        bottom_buttons.append(
            InlineKeyboardButton("⬅️", callback_data=samples.page.format(prevPage))
        )
    else:
        bottom_buttons.append(InlineKeyboardButton("⛔️", callback_data="stop"))

    bottom_buttons.append(
        InlineKeyboardButton(f"{current_page}/{total_pages}", callback_data="all_list")
    )

    if current_page == total_pages:
        bottom_buttons.append(InlineKeyboardButton("⛔️", callback_data="stop"))
    else:
        bottom_buttons.append(
            InlineKeyboardButton("➡️", callback_data=samples.page.format(next_page))
        )

    buttons.append(bottom_buttons)

    keyboard = InlineKeyboardMarkup(row_width=1, inline_keyboard=buttons)

    return keyboard
