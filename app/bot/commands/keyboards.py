from aiogram.types import (
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

user_keyboard_subscribe = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
)
user_keyboard_subscribe.add("subscribe(status)")

user_keyboard_unsubscribe = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
)
user_keyboard_unsubscribe.add("unsubscribe")


def actions_keyboard(id, page):
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(text="add", callback_data=f"add#{id}"),
        InlineKeyboardButton(text="ban", callback_data=f"ban#{id}"),
        InlineKeyboardButton(text="refusal", callback_data=f"refusal#{id}"),
        InlineKeyboardButton(text="⬅️", callback_data=f"page#{page}"),
    )
    return markup


async def pagination_keyboard(data):
    buttons = []
    current_page = data["current_page"]
    for x in data["result"]:
        user_button = [
            InlineKeyboardButton(
                f"{x.name} id : {x.id}", callback_data=f"id#{x.id}_{current_page}"
            )
        ]
        buttons.append(user_button)

    bottom_buttons = []
    if data["current_page"] != 1:
        prevPage = data["prev_page"]
        bottom_buttons.append(
            InlineKeyboardButton("⬅️", callback_data=f"page#{prevPage}")
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
            InlineKeyboardButton("➡️", callback_data=f"page#{nextPage}")
        )

    buttons.append(bottom_buttons)

    keyboard = InlineKeyboardMarkup(row_width=1, inline_keyboard=buttons)

    return keyboard
