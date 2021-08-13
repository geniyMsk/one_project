from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

progress = InlineKeyboardMarkup(
    inline_keyboard=[
        [
           InlineKeyboardButton(text='Ввести достижение', callback_data='progress')
        ]
    ])