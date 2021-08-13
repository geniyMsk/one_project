import datetime

from loader import bot, dp, scheduler
from aiogram import types
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove, ParseMode, ReplyKeyboardMarkup, KeyboardButton
import dir.DBCommands as db
import dir.states as states
import dir.keyboard as kb



@dp.message_handler(commands='start', state='*')
async def start(message: Message):
    chat_ids = db.get_all_chat_id()
    chat_id = message.from_user.id

    if (chat_id,) not in chat_ids:

        name = message.from_user.full_name
        username = message.from_user.username
        args = message.get_args()

        db.add_user(chat_id, name, username, args)
        await message.answer('Введите время, в которое вам напомнить ввести достижения (в формате чч:мм)')
        await states.state.SET_TIME.set()


@dp.message_handler(state=states.state.SET_TIME)
async def set_time(message: Message):
    a = message.text.split(':')
    if len(a) != 2 or int(a[0])< 0 or int(a[0])>23 or int(a[1])< 0 or int(a[1])>59:
        await message.answer('Вы неправильно ввел время. Вводите в формате чч:мм')
        return
    hour = int(a[0])
    minute = int(a[1])
    time = datetime.time(hour, minute)
    phrase = db.get_random_notify_phrase()
    async def notify():
        await bot.send_message(message.from_user.id, phrase, reply_markup=kb.progress, parse_mode=ParseMode.HTML)
    scheduler.add_job(notify, "cron", hour=hour, minute = minute)
    db.add_job(message.from_user.id, time)
    await bot.send_message(message.from_user.id ,'Можешь отравить своё достижение в любое время, в заданное ранее'
                                                 ' время бот тебе об этом напомнит', reply_markup=kb.progress)
    await states.state.ZERO.set()



@dp.callback_query_handler(lambda c: c.data == 'progress', state='*')
async def send_progress(call: CallbackQuery):
    i = db.count_progress(call.from_user.id)
    if i == 5:
        await bot.send_message(call.from_user.id, "Вы уже ввели 5 достижений")
        return
    await bot.send_message(call.from_user.id, "Отправь своё достижение")
    await states.state.INPUT_PROGRESS.set()


@dp.message_handler(state=states.state.INPUT_PROGRESS)
async def input_progress(message: Message):
    db.add_progress(message.from_user.id, message.text)
    await message.answer(db.get_random_motivating_phrase())
    await states.state.ZERO.set()