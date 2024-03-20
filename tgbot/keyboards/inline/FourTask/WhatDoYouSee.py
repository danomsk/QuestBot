from aiogram.types import  ReplyKeyboardMarkup, KeyboardButton

see = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(
                text="Да, я как раз сейчас вижу кое-что необычное🤔",
                callback_data="similar"
            ),
            KeyboardButton(
                text="А что сказать? Ну... 🍌",
                callback_data="banan"
            )
        ]
    ], resize_keyboard=False)
