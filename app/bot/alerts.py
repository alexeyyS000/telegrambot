import telebot
from .config import AdminSettings


def funding_alert(users_id: list, fundings: list):
    API_TOKEN = AdminSettings().bot_token
    message_string = ""
    for i in fundings:
        message_string += (
            "\n" + " " + str(i.symbol) + " " + str(i.rate) + " " + str(i.date_time)
        )
    bot = telebot.TeleBot(API_TOKEN)
    for i in users_id:
        bot.send_message(i, message_string)
