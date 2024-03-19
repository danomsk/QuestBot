from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

yes_or_no = ReplyKeyboardMarkup([
    [
        KeyboardButton("Да"),
        KeyboardButton("Нет")
    ]
],resize_keyboard=True)
