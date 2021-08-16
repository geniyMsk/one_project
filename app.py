# -*- coding: utf8 -*-


import logging
from aiogram import executor
from utils import on_startup_notify
from loader import dp, scheduler
import handlers
from aiogram.types import ParseMode, BotCommand, BotCommandScopeChat
from config import ADMINS
from loader import scheduler, bot

import dir.DBCommands as db
import dir.keyboard as kb


async def on_startup(dispatcher):
    await on_startup_notify(dispatcher)
    jobs = db.get_all_job()
    for job in jobs:
        async def notify():
            phrase = db.get_random_notify_phrase()
            await bot.send_message(job.chat_id, phrase, reply_markup=kb.progress, parse_mode=ParseMode.HTML)

        hour = job.time.hour
        minute = job.time.minute
        scheduler.add_job(notify, "cron", hour=hour, minute=minute)


    for admin in ADMINS:
        try:
            await bot.set_my_commands(commands=[BotCommand(command='logging', description='Выгрузка логирования')],
                                      scope=BotCommandScopeChat(chat_id=admin))
        except Exception as error:
            logging.exception(error)

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