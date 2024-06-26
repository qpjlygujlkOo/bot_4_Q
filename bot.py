import telebot
#import config1
import time
import os
import random
import threading
import logging
import datetime
import schedule
from threading import Thread
from dotenv import load_dotenv
from os.path import join, dirname
from time import sleep
from telebot import types, util
from bs4 import BeautifulSoup
import json
from pytz import timezone
import pytz

now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
logger = telebot.logger
logging.basicConfig(filename = f'{now}_logs.log', level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')


# print(logging.__file__)
# logger = telebot.logger
# logging.basicConfig(filename='logs.log',
#                     format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.debug("A DEBUG Message")
# logging.info("An INFO")
# logging.warning("A WARNING")
# logging.error("An ERROR")
# logging.critical("A message of CRITICAL severity")

#token = os.environ['TOKEN']
def get_from_env(key):
    dotenv_path = join(dirname(__file__), 'tokens.env')
    load_dotenv(dotenv_path)
    return os.environ.get(key)


token = get_from_env('TG_BOT_TOKEN')
bot = telebot.TeleBot(token)
print(logging.__file__)
f = open('dict.txt', 'r', encoding='utf-8')
list = f.read().split('\n')
dict = tuple(list)


def main():
    # ...
    port = os.getenv('PORT', default=8000)
    updater.start_webhook(port=port)


# bot = telebot.TeleBot(config1.TOKEN)


key = (token)
qa1 = ('@Igor_Kirichek, @lexm18, @glatemalin, @Azamat_Gu, @lena596, @Tres568')
tl1 = ('@barysh_vn, @oblivantseva')
tlqa = ('@gryzb1')
back1 = ('@mmeiko, @barysh_vn, @DmitryChernoyarov, @MaximB98, @av_sorokin, @AKS2001')
front1 = ('@chimir, @a2aev, @R071Nx')
pm1 = ('@Becky_Bones, @OlgaStupenkova, @agantts')
aqa1 = ('@glatemalin, @Azamat_Gu')
dnr1 = "на обед"
dnr2 = "кушать"
dnr3 = "кушоц"
dnr4 = "кушац"
dnr5 = "пойду поем"
dnr6 = "ушел на обед"
dnr7 = "ушел пообедать"
dnr8 = "пообедаю"
dnr9 = "я с вами"
dnr10 = "подождите меня"
dnr11 = "я тоже пойду поем"
dnr12 = "я тоже на обед"
dnr13 = "кушот"
dnr14 = "кушоть"
dnr15 = "тоже на обед"
dnr16 = "обедать"
dnr17 = "ушёл на обед"
dnr18 = "покушать"
dnr19 = "покушаю"
dnr20 = "тоже покушать"
dnr21 = "пора покушать"
dnr22 = "обед"

lunch_synonyms = [
    "на обед",
    "кушать",
    "кушоц",
    "кушац",
    "пойду поем",
    "ушел на обед",
    "ушел пообедать",
    "пообедаю",
    "я с вами",
    "подождите меня",
    "я тоже пойду поем",
    "я тоже на обед",
    "кушот",
    "кушоть",
    "тоже на обед",
    "обедать",
    "ушёл на обед",
    "покушать",
    "покушаю",
    "тоже покушать",
    "пора покушать",
    "обед",
    "покушот",
    "пол обеда",
    "половинка обеда",
    "1/2 обеда",
    "полобеда",
    "2/4 обеда",
    "обед / 2",
    "обед/2",
    "0.5 обеда",
    "0,5 обеда"
]


aza = "Azamat_Gu"
igor2 = "Igor_Kirichek"
ats = "a2aev"

dnrstc1 = "AgADAgADA8KlDg"
dnrstc2 = "AgADZgADqregFw"

chatids = [-1001210129344]
# @bot.message_handler(commands=['key'])

# def key(message):
#     bot.send.message(message.chat.id, 'токен' + key.format(message.from_user, bot.get_me()),parse_mode='html')


@bot.message_handler(commands=['qa'])
def qa(message):
    pin_qa = bot.send_message(message.chat.id,'Тестировщики! \n' + qa1.format(message.from_user, bot.get_me()),parse_mode='html').message_id
    bot.pin_chat_message(chat_id=message.chat.id, message_id=pin_qa)
    time.sleep(60)
    bot.unpin_chat_message(chat_id=message.chat.id, message_id=pin_qa)


@bot.message_handler(content_types=['pinned_message'])
def delpin(pinned_message: types.Message):
    msg = pinned_message.from_user

    if 'meetingeveryone_bot' in msg.username:
        time.sleep(120)
        bot.delete_message(pinned_message.chat.id, pinned_message.id)
    else:
        return False


@bot.message_handler(commands=['tl'], func=lambda message: message.chat.id in chatids)
def tl(message):
    bot.send_message(message.chat.id,'Тимлиды! \n' + tl1.format(message.from_user, bot.get_me()),parse_mode='html')


@bot.message_handler(commands=['front'], func=lambda message: message.chat.id in chatids)
def front(message):
    bot.send_message(message.chat.id,'Фронты! \n' + front1.format(message.from_user, bot.get_me()),parse_mode='html')


@bot.message_handler(commands=['back'], func=lambda message: message.chat.id in chatids)
def back(message):
    bot.send_message(message.chat.id,'Бэки! \n' + back1.format(message.from_user, bot.get_me()),parse_mode='html')


@bot.message_handler(commands=['pm'], func=lambda message: message.chat.id in chatids)
def mgr(message):
    bot.send_message(message.chat.id,'Манажеры! \n' + pm1.format(message.from_user, bot.get_me()),parse_mode='html')


@bot.message_handler(commands=['aqa'], func=lambda message: message.chat.id in chatids)
def aqa(message):
    bot.send_message(message.chat.id,'Авто<s>боты</s>тестировщики! \n' + aqa1.format(message.from_user, bot.get_me()), parse_mode='html')


@bot.message_handler(commands=['all'])
# , func=lambda message: message.chat.id in chatids
def all(message):
    pin_all = bot.send_message(message.chat.id,'ТОВАРИЩИ! \n' +   qa1 + ' ' + tl1 + ' ' + back1 + ' ' + front1 + ' ' + pm1.format(message.from_user, bot.get_me()), parse_mode='html').message_id
    bot.pin_chat_message(chat_id=message.chat.id, message_id=pin_all)
    sleep(1)
    bot.unpin_chat_message(chat_id=message.chat.id, message_id=pin_all)


@bot.message_handler(commands=['meet'], func=lambda message: message.chat.id in chatids)
def meetup(message):
    sti = open('stick/sticker.webp', 'rb')

    pin_meet = bot.send_message(message.chat.id,'МИТИНГ! \n' + qa1 + ' ' + tl1 + ' ' + back1 + ' ' + front1 + ' ' + pm1.format(message.from_user, bot.get_me()),parse_mode='html').message_id
    bot.pin_chat_message(chat_id=message.chat.id, message_id=pin_meet)
    bot.unpin_chat_message(chat_id=message.chat.id, message_id=pin_meet)
    time.sleep(2)
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, f'https://meet.google.com/bxq-nsek-ept')


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if (message.from_user.username == aza) and (message.text.casefold() in lunch_synonyms):
        exp = open('gif/exp3.gif', 'rb')
        bot.send_message(message.chat.id, f'ب الهناء والشفاء / بالهنا والشف!, {message.from_user.first_name}!')
        bot.send_animation(message.chat.id, exp)
    elif (message.from_user.username == igor2) and (message.text.casefold() in lunch_synonyms):
        bon = random.choice(dict)
        bot.send_message(message.chat.id, f'{bon}, Игорямба!')
        print(message.chat.id)
    elif (message.from_user.username == ats) and (message.text.casefold() in lunch_synonyms):
        bon = random.choice(dict)
        atsa = open('gif/ats.gif', 'rb')
        bot.send_message(message.chat.id, f'{bon}, {message.from_user.first_name}!')
        bot.send_animation(message.chat.id, atsa)
    #     elif (message.from_user.username == zhe) and (message.text.casefold() in lunch_synonyms):
    # #       bon = random.choice(dict)
    #         igor1 = open('gif/zhe.jpg', 'rb')
    #         bot.send_photo(message.chat.id, igor1)
    #
    #        bot.send_message(message.chat.id, f'{bon}, {message.from_user.first_name}!')
    #         bot.send_photo(message.chat.id, igor1)
    #             def cb():
    #                 bot.send_message(message.chat.id, '@Igor_Kirichek с возвращением Игорь!')
    #
    #             delay = 3600
    #             timer = threading.Timer(delay, cb)
    #             timer.start()
    elif message.text.casefold() in lunch_synonyms:
        bon = random.choice(dict)
        bot.send_message(message.chat.id, f'{bon}, {message.from_user.first_name}!')
        print(message.chat.id)

#@bot.message_handler(content_types=["sticker"])

#def handle_docs_audio(message):
#    if message.text.casefold() == dnr1:
#        bot.send_message(message.chat.id, f'Приятного аппетита, {message.from_user.first_name}, {message.file_unique_id}!')
# gavna()


@bot.message_handler(commands=['hello'])
def otkrytka1():
    # print(chatid)
    #     print(message.chat.id)
    #     global chatid
    #     chatid = message.chat.id
    dirpath = "img"
    photofile = os.listdir('img')
    random_photo = random.choice(photofile)
    fullpath = os.path.join(dirpath, random_photo)
    with open(fullpath, 'rb') as f:
        bot.send_photo(-1001210129344, f)
    # return schedule.CancelJob


@bot.message_handler(commands=['hello'])
def otkrytka2():
    # print(chatid)
    #     print(message.chat.id)
    #     global chatid
    #     chatid = message.chat.id
    dirpath = "img"
    photofile = os.listdir('img')
    random_photo = random.choice(photofile)
    fullpath = os.path.join(dirpath, random_photo)
    with open(fullpath, 'rb') as f:
        bot.send_photo(110309785, f)

# Попытка переиграть Черноярова

# @bot.message_handler(content_types=['sticker', 'document', 'photo'])
# def handle_sticker(message):
#    print(message.chat.id, message, file=open('messages.txt', 'a'))
#    stickersize = message.sticker.file_size
#    # photosize = message.photo[0].file_size
#    sender = message.from_user.username
#    # print(photosize)
#    print(stickersize)
#    if stickersize == 25316:
#        # if sender == 'DmitryChernoyarov':
#        bon = random.choice(dict)
#        bot.send_message(message.chat.id, f'{bon}, {message.from_user.first_name}!')
#        print('соси')
#     elif (stickersize == 25316342424):
#         print('несоси')
# @bot.message_handler()
# def idchata(message):
#     hz = bot.send_message(message.chat.id,message.chat.id)
#     print(message.chat.id)
#     global chatid
#     chatid = message.chat.id


def lol():
    schedule.every().monday.at("10:00", "Europe/Moscow").do(otkrytka1)
    schedule.every().tuesday.at("10:00", "Europe/Moscow").do(otkrytka1)
    schedule.every().wednesday.at("10:00", "Europe/Moscow").do(otkrytka1)
    schedule.every().thursday.at("10:00", "Europe/Moscow").do(otkrytka1)
    schedule.every().friday.at("10:00", "Europe/Moscow").do(otkrytka1)

    while True:
        schedule.run_pending()
        time.sleep(1)


def abc():
    schedule.every().monday.at("10:00", "Europe/Moscow").do(otkrytka2)
    schedule.every().tuesday.at("10:00", "Europe/Moscow").do(otkrytka2)
    schedule.every().wednesday.at("10:00", "Europe/Moscow").do(otkrytka2)
    schedule.every().thursday.at("10:00", "Europe/Moscow").do(otkrytka2)
    schedule.every().friday.at("10:00", "Europe/Moscow").do(otkrytka2)
    #
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)


def main_loop():
    thread = Thread(target=lol)
    threads = Thread(target=abc)
    thread.start()
    threads.start()

    while True:
        try:
            bot.polling(none_stop=True)  # падает на Mac
            # bot.infinity_polling()
        except Exception as ex:
            print(ex)
            sleep(15)
            # pass

# schedule.every().second.do(utre4ko)


# while True:
#     schedule.run_pending()
#     time.sleep(1)

if __name__ == '__main__':
    main_loop()

# bot.polling(none_stop=True)
