import datetime

from aiogram.dispatcher.filters import IDFilter

from loader import bot, dp, scheduler
from config import ADMINS
from aiogram import types
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove, ParseMode, ReplyKeyboardMarkup, KeyboardButton
import dir.DBCommands as db
import dir.states as states
import dir.keyboard as kb

def logging_message(message):
    f = open(f'logs/{message.from_user.id}.txt', 'a')
    time = datetime.datetime.now()
    log_time = time.strftime("%d-%b-%y %H:%M:%S")
    f.write(f'[{log_time}]      Message: {message.text}\n')
    f.close()


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



@dp.message_handler(state=states.state.SET_TIME)
async def set_time(message: Message):
    logging_message(message)
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



@dp.message_handler(text = 'Ввести достижение', state='*')
async def send_progress(message: Message):
    logging_message(message)
    i = db.count_progress(message.from_user.id)
    if i == 5:
        await bot.send_message(message.from_user.id, "Вы уже ввели 5 достижений")
        return
    await bot.send_message(message.from_user.id, "Отправь своё достижение")
    await states.state.INPUT_PROGRESS.set()


@dp.message_handler(state=states.state.INPUT_PROGRESS)
async def input_progress(message: Message):
    logging_message(message)
    db.add_progress(message.from_user.id, message.text)
    await message.answer(db.get_random_motivating_phrase(), parse_mode=ParseMode.HTML)
    await states.state.ZERO.set()


@dp.message_handler(text = 'Выгрузить свои достижения', state='*')
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
            f.write(x.text + '\n')
        f.close()
        await message.answer_document(open(file_name, 'rb'), caption='Список ваших достижений')
    except:
        await message.answer('У вас пока нет достижений')



@dp.message_handler(commands='logging', user_id=ADMINS, state='*')
async def random_messages(message: Message):
    logging_message(message)
    await message.answer_document(open(r'logs.log', 'rb'))




@dp.message_handler(state='*')
async def random_messages(message: Message):
    logging_message(message)
    await message.answer('Я вас не понял. Чтобы ввести достижение нажмите кнопку ниже')