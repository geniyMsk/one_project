# -*- coding: utf-8 -*-
import logging
import datetime
from aiogram import Dispatcher
from aiogram.types import ParseMode, BotCommand, BotCommandScope, BotCommandScopeChat

from config import ADMINS
from loader import scheduler, bot

import dir.DBCommands as db
import dir.keyboard as kb


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            pass
        except Exception as err:
            logging.error(err)

def logging_message(message):
    try:
        f = open(f'logs/{message.from_user.id}.txt', 'a')
        time = datetime.datetime.now()
        log_time = time.strftime("%d-%b-%y %H:%M:%S")
        f.write(f'[{log_time}]      Сообщение: {message.text}\n')
        f.close()
    except UnicodeEncodeError:
        pass


def logging_send_ref(query):
    try:
        f = open(f'logs/{query["from"]["id"]}.txt', 'a')
        time = datetime.datetime.now()
        log_time = time.strftime("%d-%b-%y %H:%M:%S")
        f.write(f'[{log_time}]      Отправил реферальную ссылку\n')
        f.close()
    except UnicodeEncodeError:
        pass