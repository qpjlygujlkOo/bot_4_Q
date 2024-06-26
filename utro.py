import schedule
import os
import random
import time


# def oo(bot):
#
#     @bot.message_handler(content_types='text')
#     def otkrytka():
#
#         dirpath = "img"
#         photofile = os.listdir('img')
#         random_photo = random.choice(photofile)
#         fullpath = os.path.join(dirpath, random_photo)
#         with open(fullpath, 'rb') as f:
#             bot.send_photo(71931403, photo=f)
#     schedule.every(100).seconds.do(otkrytka)


def fake_func():

    pass


def fake_func1():

    schedule.every(10).days.do(fake_func)
    while True:
        schedule.run_pending()
        time.sleep(1)


def utro_chat(bot):
    def utro_chat_i():

        dirpath = "img"
        photofile = os.listdir('img')
        random_photo = random.choice(photofile)
        fullpath = os.path.join(dirpath, random_photo)
        with open(fullpath, 'rb') as f:
            bot.send_photo(-1001210129344, f)

    schedule.every().monday.at("10:00", "Europe/Moscow").do(utro_chat_i)
    schedule.every().tuesday.at("10:00", "Europe/Moscow").do(utro_chat_i)
    schedule.every().wednesday.at("10:00", "Europe/Moscow").do(utro_chat_i)
    schedule.every().thursday.at("10:00", "Europe/Moscow").do(utro_chat_i)
    schedule.every().friday.at("10:00", "Europe/Moscow").do(utro_chat_i)


def utro_anastas(bot):

    def utro_anastas_i():
        dirpath = "img"
        photofile = os.listdir('img')
        random_photo = random.choice(photofile)
        fullpath = os.path.join(dirpath, random_photo)
        with open(fullpath, 'rb') as f:
            bot.send_photo(110309785, f)

    schedule.every().monday.at("10:00", "Europe/Moscow").do(utro_anastas_i)
    schedule.every().tuesday.at("10:00", "Europe/Moscow").do(utro_anastas_i)
    schedule.every().wednesday.at("10:00", "Europe/Moscow").do(utro_anastas_i)
    schedule.every().thursday.at("10:00", "Europe/Moscow").do(utro_anastas_i)
    schedule.every().friday.at("10:00", "Europe/Moscow").do(utro_anastas_i)
