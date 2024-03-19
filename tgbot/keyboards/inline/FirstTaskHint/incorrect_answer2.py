from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

incorrect2 = InlineKeyboardMarkup(row_width=1,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(
                                             text="2 Подсказка",
                                             callback_data="Hint2"
                                         )
                                     ]
                                 ])
