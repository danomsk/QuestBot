from aiogram import Dispatcher
from aiogram.types import Message

async def user_start(message: Message):
    await message.reply("Эх, к сожалению этот бот предназначен не для тебя(\nТак что свали пожалуйста!")
    print(message.from_user.id)


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
