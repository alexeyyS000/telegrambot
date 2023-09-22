import telebot
from bot.config import AdminSettings
from jinja2 import FileSystemLoader, Environment


def funding_alert(users_id: list, fundings: list):
    API_TOKEN = AdminSettings().bot_token
    file_loader = FileSystemLoader("app/templates")
    env = Environment(loader=file_loader)
    tm = env.get_template("funding.htm")
    msg = tm.render(fundings=fundings)
    bot = telebot.TeleBot(API_TOKEN)
    for i in users_id:
        bot.send_message(i, msg)
