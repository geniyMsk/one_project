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
            await dp.bot.send_message(admin, "Бот Запущен")
            pass
        except Exception as err:
            logging.exception(err)
    jobs = db.get_all_job()
    for job in jobs:
        async def notify():
            phrase = db.get_random_notify_phrase()
            await bot.send_message(job.chat_id, phrase, reply_markup=kb.progress, parse_mode=ParseMode.HTML)
        hour = job.time.hour
        minute = job.time.minute
        scheduler.add_job(notify, "cron", hour = hour, minute = minute)
    await bot.set_my_commands(commands=[BotCommand(command='logging', description='Выгрузка логирования')],
                              scope=BotCommandScopeChat(chat_id=admin))


