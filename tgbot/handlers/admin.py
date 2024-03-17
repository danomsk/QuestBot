from aiogram import Dispatcher
from aiogram.types import Message

from loader import config
from tgbot.config import Config




async def admin_start(message: Message):
    await message.answer("Админ, я запущен!")

def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start,  commands=["start"], state="*", is_admin=True)
