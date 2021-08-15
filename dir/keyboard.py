from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

progress = ReplyKeyboardMarkup(
    keyboard=[
        [
           KeyboardButton(text='Ввести достижение')
        ],
        [
           KeyboardButton(text='Выгрузить свои достижения')
        ]
    ], resize_keyboard=True)