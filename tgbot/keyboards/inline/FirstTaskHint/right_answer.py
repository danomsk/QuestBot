from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

answer_keyboard = InlineKeyboardMarkup(row_width=1,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(
                                             text="Ответ",
                                             callback_data="answer"
                                         )
                                     ]
                                 ])
