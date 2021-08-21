# -*- coding: utf-8 -*-
import datetime
import logging

from aiogram.dispatcher import filters

from loader import bot, dp, scheduler
from config import ADMINS
from aiogram import types
from aiogram.types import Message, CallbackQuery, ParseMode, InlineKeyboardMarkup, InlineKeyboardButton, \
     InlineQueryResultArticle, InputMessageContent
import dir.DBCommands as db
import dir.states as states
from dir.keyboard import keyboards
from utils import logging_message, logging_send_ref

kb = keyboards()


@dp.message_handler(commands='start', state='*')
async def start(message: Message):
    logging_message(message)
    chat_ids = db.get_all_chat_id()
    chat_id = message.from_user.id

    if (chat_id,) not in chat_ids:

        name = message.from_user.full_name
        username = message.from_user.username
        args = message.get_args()

        db.add_user(chat_id, name, username, args)
        await message.answer('Введите время, в которое вам напомнить ввести достижения (в формате чч:мм)')
        await states.state.SET_TIME.set()
    else:
        await message.answer(f'Привет, {message.from_user.first_name}', reply_markup=kb.progress)


@dp.message_handler(filters.Text(contains = 'Выгрузить свои достижения'), state='*')
async def send_progress(message: Message):
    logging_message(message)
    try:
        progress = db.get_progress(message.chat.id)
        file_name = f'uploads/{message.from_user.id}.txt'

        f = open(file_name, 'w')
        f.write('')
        f.close()

        f = open(file_name, 'a')
        for x in progress:
            f.write(f'Дата: {x.dt.date()}    Достижение: ' + x.text + '\n')
        f.close()
        await message.answer_document(open(file_name, 'rb'), caption='Список ваших достижений')
    except:
        await message.answer('У вас пока нет достижений')



@dp.message_handler(filters.Text(contains = 'Ввести достижение'), state='*')
async def set_progress(message: Message):
    logging_message(message)
    try:
        i = db.count_progress(message.from_user.id)
        if i == 5:
            await bot.send_message(message.from_user.id, "Вы уже ввели 5 достижений")
            return
        await bot.send_message(message.from_user.id, "Отправь своё достижение")
        await states.state.INPUT_PROGRESS.set()
    except Exception as error:
        logging.error(error)

@dp.message_handler(filters.Text(contains = 'Дополнительно'), state='*')
async def additionally(message: Message):
    logging_message(message)
    try:
        await message.answer('Дополнительно', reply_markup=kb.add)
    except Exception as error:
        logging.error(error)


@dp.message_handler(filters.Text(contains = 'Поделиться ботом'), state='*')
async def ref_link(message: Message):
    logging_message(message)
    try:
        await message.answer('Перешлите сообщение ниже')
        bot_username = (await bot.get_me()).username
        await message.answer('Нажми кнопку поделиться, чтобы отправить бота друзьям и подругам',
                             reply_markup=kb.get_ref_keyboard(url=f't.me/{bot_username}?start=k{message.from_user.id}'))

    except Exception as error:
        logging.error(error)


@dp.message_handler(filters.Text(contains = 'Поблагодарить'), state='*')
async def thank(message: Message):
    try:
        await message.answer(db.get_random_thank_phrase())
    except Exception as error:
        logging.error(error)


@dp.message_handler(filters.Text(contains = 'Время напоминания'), state='*')
async def time(message: Message):
    try:
        time = db.get_job(message.chat.id)
        if time is not None:
            await message.answer(f'Напоминания будут приходить в {time.time.strftime("%H:%M")} МСК',
                                                                                           reply_markup=kb.change_time)
        else:
            await message.answer(f'Время не установлено, чтобы установить - нажмите кнопку ниже',
                                 reply_markup=kb.change_time)
    except Exception as error:
        logging.error(error)


@dp.callback_query_handler(text = 'change_time', state='*')
async def change_time(call: CallbackQuery):
    try:
        await bot.send_message(call.message.chat.id,
                               'Введите время, в которое вам напомнить ввести достижения (в формате чч:мм)')
        await states.state.SET_TIME.set()
    except Exception as error:
        logging.error(error)


@dp.message_handler(filters.Text(contains = 'Обратная связь'), state='*')
async def back(message: Message):
    try:
        await message.answer('текст допишу')
    except Exception as error:
        logging.error(error)


@dp.message_handler(filters.Text(contains = 'Назад'), state='*')
async def back(message: Message):
    try:
        await message.answer(f'Привет, {message.from_user.first_name}', reply_markup=kb.progress)
    except Exception as error:
        logging.error(error)


'''
@dp.inline_handler(state='*')
async def sa(query: types.InlineQuery):
    try:
        bot_username = (await bot.get_me()).username
        result = [InlineQueryResultArticle(
            id='1', title='Реферальная ссылка', description='Нажмите для отправки реферальной ссылки',
            reply_markup=kb.get_ref_keyboard(url=f't.me/{bot_username}?start=k{query.from_user.id}'),
            input_message_content = InputMessageContent(
                message_text=f'Перейди по моей ссылке')
        )]
        await bot.answer_inline_query(query.id, result, cache_time=1)
    except Exception as error:
        logging.error(error)

@dp.chosen_inline_handler(state='*')
async def choosen(query: types.ChosenInlineResult):
    try:
        logging_send_ref(query)
    except Exception as error:
        logging.error(error)
'''