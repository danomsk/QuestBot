from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

incorrect1 = InlineKeyboardMarkup(row_width=1,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(
                                             text="1 Подсказка",
                                             callback_data="Hint1"
                                         )
                                     ]
                                 ])
