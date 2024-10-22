import time as t
from datetime import *
from variables import *
from telebot import types


def qa(bot):

    @bot.message_handler(commands=['qa'])
    def qaa(message):
        qatime = datetime.now()
        dnd = qatime.strftime("%H")
        print(qatime.strftime("%H"))
        if dnd in work_hours:
            pin_qa = bot.send_message(message.chat.id, 'Тестировщики! \n' + qa1.format(message.from_user, bot.get_me()),
                                  parse_mode='html').message_id
            bot.pin_chat_message(chat_id=message.chat.id, message_id=pin_qa)
            t.sleep(30)
            bot.unpin_chat_message(chat_id=message.chat.id, message_id=pin_qa)

        elif dnd in qa_rest:
            bot.send_message(message.chat.id, 'Тестировщики ужо адыхают')

        elif dnd in qa_sleep:
            bot.send_message(message.chat.id, 'Тестировщики еще спять')

    @bot.message_handler(commands=['tl'])
    def tl(message):
        if message.chat.id == chatidTestir:
            bot.send_message(message.chat.id, 'Тимлиды! \n' + tl1.format(message.from_user, bot.get_me()),
                             parse_mode='html')
        else:
            pass

    @bot.message_handler(commands=['front'])
    def front(message):
        if message.chat.id == chatidTestir:
            bot.send_message(message.chat.id, 'Фронты! \n' + front1.format(message.from_user, bot.get_me()),
                             parse_mode='html')
        else:
            pass

    @bot.message_handler(commands=['back'])
    def back(message):
        if message.chat.id == chatidTestir:
            bot.send_message(message.chat.id, 'Бэки! \n' + back1.format(message.from_user, bot.get_me()),
                             parse_mode='html')
        else:
            pass

    @bot.message_handler(commands=['pm'])
    def mgr(message):
        if message.chat.id == chatidTestir:
            bot.send_message(message.chat.id, 'Манажеры! \n' + pm1.format(message.from_user, bot.get_me()),
                             parse_mode='html')
        else:
            pass

    @bot.message_handler(commands=['aqa'])
    def aqa(message):
        if message.chat.id == chatidTestir:
            bot.send_message(message.chat.id, 'Авто<s>боты</s>тестировщики! \n' + aqa1.format(message.from_user,
                             bot.get_me()), parse_mode='html')
        else:
            pass

    @bot.message_handler(commands=['all'])
    def all(message):
        if message.chat.id == chatidTestir:
            pin_all = bot.send_message(message.chat.id, 'ТОВАРИЩИ! \n' + qa1 + ' ' + tl1 + ' ' + back1 + ' ' + front1 +
                                       ' ' + pm1.format(message.from_user, bot.get_me()), parse_mode='html').message_id
            bot.pin_chat_message(chat_id=message.chat.id, message_id=pin_all)
            time.sleep(30)
            bot.unpin_chat_message(chat_id=message.chat.id, message_id=pin_all)
        else:
            pass

    @bot.message_handler(commands=['meet'])
    def meetup(message):
        if message.chat.id == chatidTestir:
            sti = open('stick/sticker.webp', 'rb')

            pin_meet = bot.send_message(message.chat.id, 'МИТИНГ! \n' + qa1 + ' ' + tl1 + ' ' + back1 + ' ' + front1 +
                                        ' ' + pm1.format(message.from_user, bot.get_me()), parse_mode='html').message_id
            bot.pin_chat_message(chat_id=message.chat.id, message_id=pin_meet)
            bot.send_sticker(message.chat.id, sti)
            bot.send_message(message.chat.id, f'https://meet.google.com/bxq-nsek-ept')
            time.sleep(30)
            bot.unpin_chat_message(chat_id=message.chat.id, message_id=pin_meet)
            time.sleep(2)

        else:
            pass

    @bot.message_handler(commands=['tlqqq'])
    def whatmsg(message):
        try:
            msg = bot.send_message(71931403, 'что пишем?')
            bot.register_next_step_handler(msg, msgtochat)
        except Exception as e:
            bot.send_message(71931403, 'ex!!')

    def msgtochat(message):
        try:
            bot.send_message(-1001210129344, message.text)
        except Exception as e:
            bot.send_message(71931403, 'ex')

    @bot.message_handler(content_types=['pinned_message'])
    def delpin(pinned_message: types.Message):
        msg = pinned_message.from_user

        if 'meetingeveryone_bot' in msg.username:
            time.sleep(30)
            bot.delete_message(pinned_message.chat.id, pinned_message.id)
        else:
            pass
