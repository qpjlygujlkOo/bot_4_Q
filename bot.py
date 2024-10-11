import telebot
from telebot import TeleBot
from telebot.types import Message
from telebot import types, util
import asyncio

import os
from os.path import join, dirname
from dotenv import load_dotenv

import threading
from threading import Thread

import time
from time import sleep
import datetime
import schedule

import random

import logging

import utro
import delpin
import commands
import dinner
from utro import fake_func1
from commands import qa
from dinner import obed
from delpin import pindel

# import commands
# from bs4 import BeautifulSoup
# import json
# from pytz import timezone
# import pytz
# from variables import *


# Добавление логирования
# now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
# logger = telebot.logger
# logging.basicConfig(filename = f'{now}_logs.log', level=logging.DEBUG,
#                     format=' %(asctime)s - %(levelname)s - %(message)s')


# Подключение токена
def get_from_env(key):
    dotenv_path = join(dirname(__file__), 'tokens.env')
    load_dotenv(dotenv_path)
    return os.environ.get(key)


token = get_from_env('TG_BOT_TOKEN')
bot = telebot.TeleBot(token)
key = token


# def main():
#     # ...
#     port = os.getenv('PORT', default=8000)
#     updater.start_webhook(port=port)


# Подключение модуля команд
# qa(bot)


# Подключение модуля удаления пина
# pindel(bot)


# Подключение модуля обеда
# obed(bot)


# Подключение модуля открыток
def main_loop():
    thread = Thread(target=fake_func1)
    thread_1 = Thread(target=utro.utro_anastas(bot))
    thread_2 = Thread(target=utro.utro_chat(bot))
    # thread_3 = Thread(target=delpin.pindel(bot))
    thread_4 = Thread(target=commands.qa(bot))
    thread_5 = Thread(target=dinner.obed(bot))

    thread.start()
    thread_1.start()
    thread_2.start()
    # thread_3.start()
    thread_4.start()
    thread_5.start()

    while True:
        try:
            bot.polling(none_stop=True)  # падает на Mac
            # bot.infinity_polling()
        except Exception as ex:
            print(ex)
            sleep(1)
            pass


if __name__ == '__main__':
    main_loop()
# if __name__ == '__main__':
# bot.polling(none_stop=True)
# # bot.polling(none_stop=True)
