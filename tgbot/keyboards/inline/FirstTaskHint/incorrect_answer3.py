from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

incorrect3 = InlineKeyboardMarkup(row_width=1,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(
                                             text="3 Подсказка",
                                             callback_data="Hint3"
                                         )
                                     ]
                                 ])
