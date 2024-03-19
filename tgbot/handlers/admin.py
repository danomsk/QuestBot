from aiogram import Dispatcher
from aiogram.types import Message, ContentType

from loader import config
from tgbot.config import Config

async def admin_start(message: Message):
    await message.answer("Админ, я запущен!")

async def sticker_handler(message: Message):
    await message.answer("Ты прислал стикер")
    await message.answer(f"{message.sticker.file_id}")

async def photo_handler(message: Message):
    await message.answer("Ты прислал фото")
    await message.answer(f"{message.photo[-1].file_unique_id}")

async def get_photo(message: Message):
    await message.answer_photo(photo="AgACAgIAAxkBAAICHWX5xG6rutQqMaP_m2UuCUeN5idsAAIv2DEbcfjQSwx04GZKTG3LAQADAgADeQADNAQ")

def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start,  commands=["start"], state="*", is_admin=True)
    dp.register_message_handler(sticker_handler, content_types=ContentType.STICKER, is_admin=True)
    dp.register_message_handler(photo_handler, content_types=ContentType.PHOTO, is_admin=True)
    dp.register_message_handler(get_photo, commands=["get_photo"], is_admin=True)

