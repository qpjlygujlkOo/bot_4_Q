import datetime
from datetime import *
from variables import *
import random

f = open('dict.txt', 'r', encoding='utf-8')
list_obed = f.read().split('\n')
dict_obed = tuple(list_obed)

obed_times = {}
obed_times_half = {}


def obed(bot):
    @bot.message_handler(func=lambda message: True)
    def msg(message):
        global obed_times
        bon = random.choice(dict_obed)
        obedaet = False
        if (message.from_user.username == aza) and (message.text.casefold() in lunch_synonyms):
            exp = open('gif/cat.gif', 'rb')
            bot.send_message(message.chat.id, f'ب الهناء والشفاء / بالهنا والشف!, {message.from_user.first_name}!')
            bot.send_animation(message.chat.id, exp)
            obedaet = True
        elif (message.from_user.username == igor) and (message.text.casefold() in lunch_synonyms):
            bot.send_message(message.chat.id, f'{bon}, Игорямба!')
            obedaet = True
        elif (message.from_user.username == ats) and (message.text.casefold() in lunch_synonyms):
            atsa = open('gif/ats.gif', 'rb')
            bot.send_message(message.chat.id, f'{bon}, {message.from_user.first_name}!')
            bot.send_animation(message.chat.id, atsa)
            obedaet = True
        elif message.text.casefold() in lunch_synonyms:
            bot.send_message(message.chat.id, f'{bon}, {message.from_user.first_name}!')
            obedaet = True
        if obedaet:
            obed_times[message.from_user.username] = datetime.now()
            print(message.chat.id)

        global obed_times_half
        obedaet = False
        if (message.from_user.username == aza) and (message.text.casefold() in lunch_half):
            exp = open('gif/cat.gif', 'rb')
            bot.send_message(message.chat.id, f'ب الهناء والشفاء / بالهنا والشف!, {message.from_user.first_name}!')
            bot.send_animation(message.chat.id, exp)
            obedaet = True
        elif (message.from_user.username == igor) and (message.text.casefold() in lunch_half):
            bot.send_message(message.chat.id, f'{bon}, Игорямба!')
            obedaet = True
        elif (message.from_user.username == ats) and (message.text.casefold() in lunch_half):
            atsa = open('gif/ats.gif', 'rb')
            bot.send_message(message.chat.id, f'{bon}, {message.from_user.first_name}!')
            bot.send_animation(message.chat.id, atsa)
            obedaet = True
        elif message.text.casefold() in lunch_half:
            bot.send_message(message.chat.id, f'{bon}, {message.from_user.first_name}!')
            obedaet = True
        if obedaet:
            obed_times_half[message.from_user.username] = datetime.now()
            print(message.chat.id)

        for user in obed_times.keys():
            if user in message.text and message.from_user.id != bot.get_me().id:
                last_obed_time = obed_times[user]

                if datetime.now() < last_obed_time + timedelta(minutes=60):
                    bot.reply_to(message, 'Дай пообедать!!!')

        for user in obed_times_half.keys():
            if user in message.text and message.from_user.id != bot.get_me().id:
                last_obed_half_time = obed_times_half[user]

                if datetime.now() < last_obed_half_time + timedelta(minutes=30):
                    bot.reply_to(message, 'Дай пообедать!!!')

