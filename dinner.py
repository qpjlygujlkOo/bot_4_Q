from variables import *
import random


f = open('dict.txt', 'r', encoding='utf-8')
list = f.read().split('\n')
dict = tuple(list)


def obed(bot):
    @bot.message_handler(content_types='text')
    def msg(message):

        if (message.from_user.username == aza) and (message.text.casefold() in lunch_synonyms):
            exp = open('gif/cat.gif', 'rb')
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
        elif message.text.casefold() in lunch_synonyms:
            bon = random.choice(dict)
            bot.send_message(message.chat.id, f'{bon}, {message.from_user.first_name}!')
            print(message.chat.id)
