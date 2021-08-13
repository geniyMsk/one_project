from aiogram.dispatcher.filters.state import State, StatesGroup

class state(StatesGroup):
    ZERO = State()
    SET_TIME = State()
    INPUT_PROGRESS = State()