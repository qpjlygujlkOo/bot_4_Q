import time
from telebot import types


def pindel(bot):
    @bot.message_handler(content_types=['pinned_message'])
    def delpin(pinned_message: types.Message):
        msg = pinned_message.from_user

        if 'meetingeveryone_bot' in msg.username:
            time.sleep(60)
            bot.delete_message(pinned_message.chat.id, pinned_message.id)
        else:
            return False
кв