# -*- coding: utf8 -*-


import logging

import aiogram
from aiogram import executor
from utils import on_startup_notify
from loader import dp, scheduler
import handlers
from aiogram.types import ParseMode, BotCommand, BotCommandScopeChat
from config import ADMINS
from loader import scheduler, bot

import dir.DBCommands as db
from dir.keyboard import keyboards

kb = keyboards()

async def on_startup(dispatcher):
    await on_startup_notify(dispatcher)
    jobs = db.get_all_job()
    for job in jobs:
        async def notify():
            phrase = db.get_random_notify_phrase()
            try:
                await bot.send_message(job.chat_id, phrase, reply_markup=kb.progress, parse_mode=ParseMode.HTML)
            except aiogram.utils.exception.BotBlocked:
                pass
            except Exception as error:
                logging.error(error)


        hour = job.time.hour
        minute = job.time.minute
        j = scheduler.add_job(notify, "cron", hour=hour, minute=minute)
        db.set_job_id(job.id, j.id)


    for admin in ADMINS:
        try:
            await bot.set_my_commands(commands=[BotCommand(command='logging', description='Выгрузка логирования'),
                                                BotCommand(command='stat', description='Статистика'),
                                                BotCommand(command='sending', description='Рассылка'),
                                                BotCommand(command='count', description='Считаем живых')],
                                      scope=BotCommandScopeChat(chat_id=admin))
        except Exception as error:
            pass

log_file = 'logs.log'
f = open(log_file, 'a')
f.write('-------------------------\n')
f.close()

file_log = logging.FileHandler(log_file)
console_out = logging.StreamHandler()
logging.basicConfig(handlers=(file_log, console_out),
                    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)



if __name__ == '__main__':
    scheduler.start()
    executor.start_polling(dp, on_startup=on_startup)