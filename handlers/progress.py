# -*- coding: utf-8 -*-
import datetime
import logging

import aiogram

from loader import bot, dp, scheduler
from config import ADMINS
from aiogram import types
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove, ParseMode, ReplyKeyboardMarkup, KeyboardButton
import dir.DBCommands as db
import dir.states as states
from dir.keyboard import keyboards
from utils import logging_message

kb = keyboards()
@dp.message_handler(state=states.state.SET_TIME)
async def set_time(message: Message):
    logging_message(message)
    a = message.text.split(':')
    if len(a) != 2 or int(a[0])< 0 or int(a[0])>23 or int(a[1])< 0 or int(a[1])>59:
        await message.answer('Вы неправильно ввели время. Вводите в формате чч:мм')
        return
    hour = int(a[0])
    minute = int(a[1])
    time = datetime.time(hour, minute)

    async def notify():
        phrase = db.get_random_notify_phrase()
        try:
            await bot.send_message(message.from_user.id, phrase, reply_markup=kb.progress, parse_mode=ParseMode.HTML)
        except aiogram.utils.exceptions.BotBlocked:
            pass
        except Exception as error:
            logging.error(error)


    if db.get_job(message.chat.id):
        scheduler.remove_job(db.get_job(message.chat.id).job_id, 'default')
        db.delete_job_id(db.get_job(message.chat.id).id)


    job = scheduler.add_job(notify, "cron", hour=hour, minute = minute)
    db.add_job(message.from_user.id, time, job.id)

    await bot.send_message(message.from_user.id, 'Можешь отравить своё достижение в любое время, в заданное ранее'
                                                 ' время бот тебе об этом напомнит', reply_markup=kb.progress)
    await states.state.ZERO.set()


@dp.message_handler(state=states.state.INPUT_PROGRESS)
async def input_progress(message: Message):
    logging_message(message)
    db.add_progress(message.from_user.id, message.text)
    await message.answer(db.get_random_motivating_phrase(), parse_mode=ParseMode.HTML)
    await states.state.ZERO.set()
