import logging
import datetime
import telebot

def gavna():

    logger = telebot.logger
    telebot.logger.BasicConfig(filename='logs.log', level=logging.DEBUG,
                        format=' %(asctime)s - %(levelname)s - %(message)s') 