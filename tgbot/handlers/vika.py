from aiogram import Dispatcher
from aiogram.types import Message

from loader import bot, config
from tgbot.keyboards.inline import adventure


async def vika_start(message: Message):
    await message.answer("""Дорогая Вика, добро пожаловать в наше увлекательное приключение!🌟\n
Сегодня мы отправимся в путешествие по нашим самым важным местам, наполненным и любовью и беспечностью.💖\n
Пусть этот день станет для нас особенным, наполненным романтикой и приятными сюрпризами.\n
Готова ли ты отправиться в это незабываемое приключение со мной? 😊""",
                         reply_markup=adventure)
    await bot.send_message(chat_id=config.tg_bot.admin_ids[0], text="Она нажала на кнопку start!\nИгра началась")


def register_vika(dp: Dispatcher):
    dp.register_message_handler(vika_start, commands=["start"], state="*", is_vika=True)
