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
qa1 = ('@Igor_Kirichek, @lexm18, @from_time_to_time, @glatemalin, @inside4276, @Azamat_Gu, @lena596')
tl1 = ('@ivleonov, @oblivantseva, @av_sorokin')
tlqa = ('@gryzb1')
back1 = ('@mmeiko, @barysh_vn, @DmitryChernoyarov, @MaximB98, @nikitaSavvateev')
front1 = ('@chimir, @LM001048596B')
pm1 = ('@Becky_Bones, @OlgaStupenkova')
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

kir1 = "Azamat_Gu"
igor1 = "Igor_Kirichek"

dnrstc1 = "AgADAgADA8KlDg"
dnrstc2 = "AgADZgADqregFw"

# @bot.message_handler(commands=['key'])

# def key(message):
#     bot.send.message(message.chat.id, 'токен' + key.format(message.from_user, bot.get_me()),parse_mode='html')

@bot.message_handler(commands=['qa'])
 
def qa(message):
    bot.send_message(message.chat.id,'Тестировщики! \n' + qa1.format(message.from_user, bot.get_me()),parse_mode='html')

@bot.message_handler(commands=['tl'])
 
def tl(message):
    bot.send_message(message.chat.id,'Тимлиды! \n' + tl1.format(message.from_user, bot.get_me()),parse_mode='html')

@bot.message_handler(commands=['front'])
 
def front(message):
    bot.send_message(message.chat.id,'Фронты! \n' + front1.format(message.from_user, bot.get_me()),parse_mode='html')

@bot.message_handler(commands=['back'])
 
def back(message):
    bot.send_message(message.chat.id,'Бэки! \n' + back1.format(message.from_user, bot.get_me()),parse_mode='html')

@bot.message_handler(commands=['pm'])
 
def mgr(message):
    bot.send_message(message.chat.id,'Манажеры! \n' + pm1.format(message.from_user, bot.get_me()),parse_mode='html')

@bot.message_handler(commands=['aqa'])

def aqa(message):
    bot.send_message(message.chat.id,'Авто<s>боты</s>тестировщики! \n' + aqa1.format(message.from_user, bot.get_me()),parse_mode='html')

@bot.message_handler(commands=['all'])
 
def all(message):
    bot.send_message(message.chat.id,'ТОВАРИЩИ! \n' + qa1 + ' ' + tl1 + ' ' + front1 + ' ' + back1 + ' ' + pm1.format(message.from_user, bot.get_me()),parse_mode='html')

@bot.message_handler(commands=['meet'])
 
def meetup(message):
    sti = open('stick/sticker.webp', 'rb')

    bot.send_message(message.chat.id,'МИТИНГ! \n' + qa1 + ' ' + tl1 + ' ' + front1 + ' ' + back1 + ' ' + pm1.format(message.from_user, bot.get_me()),parse_mode='html')
    time.sleep(2)
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, f'https://meet.google.com/bxq-nsek-ept')
@bot.message_handler(content_types=['text'])

def handle_text(message):
    if (message.from_user.username == kir1) and (message.text.casefold() in lunch_synonyms):
        exp = open('gif/exp.gif', 'rb')
        bot.send_message(message.chat.id, f'ب الهناء والشفاء / بالهنا والشف!, {message.from_user.first_name}!')
        bot.send_animation(message.chat.id, exp)
    elif (message.from_user.username == igor1) and (message.text.casefold() in lunch_synonyms):
            bon = random.choice(dict)
            bot.send_message(message.chat.id, f'{bon}, Игорямба!')
            print(message.chat.id) 

#             def cb():
#                 bot.send_message(message.chat.id, '@Igor_Kirichek с возвращением Игорь!')
#
#             delay = 3600
#             timer = threading.Timer(delay, cb)
#             timer.start()
    elif (message.text.casefold() == dnr1 or message.text.casefold() in lunch_synonyms):
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
    dirpath = "img/"
    photofile = os.listdir('img')
    random_photo = random.choice(photofile)
    fullpath = os.path.join(dirpath, random_photo)
    with open(fullpath, 'rb') as f:
        bot.send_photo(-1001210129344, f)
        bot.send_photo(110309785, f)
    # return schedule.CancelJob

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
    schedule.every().day.at("10:00", "Europe/Moscow").do(otkrytka1)

    while True:
        schedule.run_pending()
        time.sleep(1)


def main_loop():
    thread = Thread(target=lol)
    thread.start()

    while(True):
        try:
            bot.polling(none_stop=True) #падает на Mac
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
