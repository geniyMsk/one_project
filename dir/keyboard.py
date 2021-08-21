from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

class keyboards():
    progress = ReplyKeyboardMarkup(
        keyboard=[
            [
               KeyboardButton(text='Ввести достижение')
            ],
            [
               KeyboardButton(text='Выгрузить свои достижения'),
               KeyboardButton(text='Дополнительно')
            ]
        ], resize_keyboard=True)

    add = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='🕊Поделиться ботом'),
                KeyboardButton(text='👏Поблагодарить'),
            ],
            [
                KeyboardButton(text='⏰Время напоминания'),
                KeyboardButton(text='👋Обратная связь')
            ],
            [
                KeyboardButton(text='Назад')
            ]
        ], resize_keyboard=True)


    sending = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Отправить', callback_data='send')
            ],
            [
                InlineKeyboardButton(text='Назад', callback_data='back')
            ]
        ])

    sending_2 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Отправить', callback_data='send')
            ],
            [
                InlineKeyboardButton(text='Отправить без звука', callback_data='send_without_notify')
            ],
            [
                InlineKeyboardButton(text='Назад', callback_data='back')
            ]
        ])

    def get_ref_keyboard(self, url):
        kb = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Перейти в бота', url=url)
                ]
            ])
        return kb

    change_time = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Поменять время напоминания', callback_data='change_time')
            ]
        ])