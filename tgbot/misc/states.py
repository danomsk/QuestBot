from aiogram.dispatcher.filters.state import StatesGroup, State


class FirstTask(StatesGroup):
    T1 = State()

class SecondTask(StatesGroup):
    T2 = State()