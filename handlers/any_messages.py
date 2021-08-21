# -*- coding: utf-8 -*-
import aiogram

from loader import dp
from aiogram.types import Message
from utils import logging_message



@dp.message_handler(state='*', content_types='any')
async def random_messages(message: Message):
    logging_message(message)
    await message.answer('Я вас не понял. Чтобы ввести достижение нажмите кнопку ниже')
