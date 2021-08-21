# -*- coding: utf-8 -*-

import datetime
import logging
import random
from asyncio import sleep

import aiogram
from aiogram.dispatcher import FSMContext

from loader import bot, dp, scheduler
from config import ADMINS, OWNERS
from aiogram import types
from aiogram.types import Message, CallbackQuery, ParseMode, MediaGroup
import dir.DBCommands as db
import dir.states as states
from dir.keyboard import keyboards
from utils import logging_message

address_to_admins = ['Господин', 'Ваше величество', 'мой Повелитель']

kb = keyboards()

@dp.message_handler(commands='logging', user_id=ADMINS, state='*')
async def send_logs(message: Message):
    await bot.send_chat_action(message.chat.id, 'typing')
    logging_message(message)
    await message.answer_document(open(r'logs.log', 'rb'))


@dp.message_handler(commands='count', user_id=ADMINS, state='*')
async def check(message: Message):
    try:
        users = db.get_all_chat_id()
        i=0
        for user in users:
            try:
                await bot.send_chat_action(user[0], 'typing')
                await sleep(0.2)
                i += 1
            except aiogram.utils.exceptions.BotBlocked:
                pass
            except Exception as error:
                logging.error(error)
                    
        for admin in ADMINS:
            try:
                await bot.send_message(admin ,f'Живо {i} из {len(users)} ({round(i/len(users) * 100,2)} %)')
                await sleep(1)
            except:
                pass

    except Exception as error:
        logging.error(error)

@dp.message_handler(commands='stat', user_id=ADMINS, state='*')
async def send_stat(message: Message):
    await bot.send_chat_action(message.chat.id, 'typing')
    try:
        users = db.get_all_users()
        progress = db.get_all_progress()

        count_users = len(users)
        reg_today = 0
        args = []
        count_args_today = {}
        for user in users:
            if user.reg_dt.date() == datetime.date.today():
                reg_today += 1
                try:
                    x = count_args_today[user.args]
                except:
                    x = 0
                if user.args is not None:
                    count_args_today[user.args] = x + 1
            if user.args not in args and user.args is not None:
                args.append(user.args)
        count_progress = len(progress)
        progress_today = 0
        for prog in progress:
            if prog.dt.date() == datetime.date.today():
                progress_today += 1

        count_args = {}
        for arg in args:
            count_args[arg] = db.count_args_users(arg)

        args_text = ''
        args_text_today = ''
        for i in count_args:
            args_text += f'{i} - {count_args[i]}\n   '
        for j in count_args_today:
            args_text_today += f'{j} - {count_args_today[j]}\n   '

        stat_file = 'stat.txt'
        f = open(stat_file, 'w')
        f.write(f'1) Общее количество пользователей:  {count_users}\n'
                f'2) Регистрации за сегодня: {reg_today}\n'
                f'3) Общее количество достижений: {count_progress}\n'
                f'4) Количество достижений за сегодня: {progress_today}\n'
                f'5) {args_text}\n'
                f'6) {args_text_today}')
        f.close()

        await message.answer_document(document=open(stat_file, 'rb'),
                                      caption=f'Ваша статистика, {random.choice(address_to_admins)}')
    except Exception as error:
        logging.error(error)


@dp.message_handler(commands='sending', user_id=OWNERS, state='*')
async def sending(message: Message):
    try:
        await message.answer(f'Жду сообщение для рассылки, {random.choice(address_to_admins)}')
        await states.admin.WAITING_SENDING.set()
    except Exception as error:
        logging.error(error)


@dp.message_handler(user_id=OWNERS, state=states.admin.WAITING_SENDING, content_types=['any'])
async def sending(message: Message, state: FSMContext):
    try:
        await state.reset_data()
        message_id = await bot.copy_message(chat_id=message.chat.id, from_chat_id=message.chat.id,
                                            message_id=message.message_id, reply_markup=kb.sending)
        data = {
            'message_id': message_id['message_id'],
            'chat_id': message.chat.id
        }
        await state.update_data(data)

        await states.admin.APPROVE.set()
    except Exception as error:
        await message.answer('Произошла ошибка')
        logging.error(error)


@dp.callback_query_handler(user_id=OWNERS, text='send', state=states.admin.APPROVE)
async def sending(call: CallbackQuery, state: FSMContext):
    try:
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup='')
        await bot.send_message(call.from_user.id, text='Как отправить рассылку?', reply_markup=kb.sending_2)
        await states.admin.SECOND_APPROVE.set()
    except Exception as error:
        await bot.send_message(call.message.chat.id, 'Произошла ошибка')
        logging.error(error)



@dp.callback_query_handler(user_id=OWNERS, text='back', state=[states.admin.APPROVE, states.admin.SECOND_APPROVE])
async def sending(call: CallbackQuery, state: FSMContext):
    try:
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await bot.send_message(call.message.chat.id,
                               f'Жду сообщение для рассылки, {random.choice(address_to_admins)}')
        await states.admin.WAITING_SENDING.set()
    except Exception as error:
        await bot.send_message(call.message.chat.id, 'Произошла ошибка')
        logging.error(error)


@dp.callback_query_handler(user_id=OWNERS, text=['send', 'send_without_notify'], state=states.admin.SECOND_APPROVE)
async def sending(call: CallbackQuery, state: FSMContext):
    if call.data == 'send':
        disable_notification = False
    elif call.data == 'send_without_notify':
        disable_notification = True
    users = db.get_all_chat_id()
    data = await state.get_data()

    message_id = data['message_id']
    from_chat_id = data['chat_id']
    i=0
    for user in users:
        try:
            await bot.copy_message(chat_id=user[0], from_chat_id=from_chat_id, message_id=message_id,
                                   disable_notification=disable_notification)
            await sleep(0.2)
            i+=1
        except aiogram.utils.exceptions.BotBlocked:
            pass
        except Exception as error:
            logging.error(error)
    try:
        await bot.send_message(call.message.chat.id, f'Доставлено {i} из {len(users)} ({round(i/len(users) * 100,2)}%)')
    except:
        pass


