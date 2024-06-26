import time
from variables import *


def qa(bot):
    @bot.message_handler(commands=['qa'])
    def qaa(message):
        pin_qa = bot.send_message(message.chat.id, 'Тестировщики! \n' + qa1.format(message.from_user, bot.get_me()),
                                  parse_mode='html').message_id
        bot.pin_chat_message(chat_id=message.chat.id, message_id=pin_qa)
        time.sleep(65)
        bot.unpin_chat_message(chat_id=message.chat.id, message_id=pin_qa)

    @bot.message_handler(commands=['tl'])
    def tl(message):
        bot.send_message(message.chat.id, 'Тимлиды! \n' + tl1.format(message.from_user, bot.get_me()),
                         parse_mode='html')

    @bot.message_handler(commands=['front'], func=lambda message: message.chat.id in chatids)
    def front(message):
        bot.send_message(message.chat.id, 'Фронты! \n' + front1.format(message.from_user, bot.get_me()),
                         parse_mode='html')

    @bot.message_handler(commands=['back'], func=lambda message: message.chat.id in chatids)
    def back(message):
        bot.send_message(message.chat.id, 'Бэки! \n' + back1.format(message.from_user, bot.get_me()), parse_mode='html')

    @bot.message_handler(commands=['pm'], func=lambda message: message.chat.id in chatids)
    def mgr(message):
        bot.send_message(message.chat.id, 'Манажеры! \n' + pm1.format(message.from_user, bot.get_me()),
                         parse_mode='html')

    @bot.message_handler(commands=['aqa'], func=lambda message: message.chat.id in chatids)
    def aqa(message):
        bot.send_message(message.chat.id, 'Авто<s>боты</s>тестировщики! \n' + aqa1.format(message.from_user,
                         bot.get_me()), parse_mode='html')

    @bot.message_handler(commands=['all'], func=lambda message: message.chat.id in chatids)
    def all(message):
        pin_all = bot.send_message(message.chat.id, 'ТОВАРИЩИ! \n' + qa1 + ' ' + tl1 + ' ' + back1 + ' ' + front1 + ' '
                                   + pm1.format(message.from_user, bot.get_me()), parse_mode='html').message_id
        bot.pin_chat_message(chat_id=message.chat.id, message_id=pin_all)
        time.sleep(65)
        bot.unpin_chat_message(chat_id=message.chat.id, message_id=pin_all)

    @bot.message_handler(commands=['meet'], func=lambda message: message.chat.id in chatids)
    def meetup(message):
        sti = open('stick/sticker.webp', 'rb')

        pin_meet = bot.send_message(message.chat.id, 'МИТИНГ! \n' + qa1 + ' ' + tl1 + ' ' + back1 + ' ' + front1 + ' ' +
                                    pm1.format(message.from_user, bot.get_me()), parse_mode='html').message_id
        bot.pin_chat_message(chat_id=message.chat.id, message_id=pin_meet)
        time.sleep(65)
        bot.unpin_chat_message(chat_id=message.chat.id, message_id=pin_meet)
        time.sleep(2)
        bot.send_sticker(message.chat.id, sti)
        bot.send_message(message.chat.id, f'https://meet.google.com/bxq-nsek-ept')

