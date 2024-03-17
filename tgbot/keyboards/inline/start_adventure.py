from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

adventure = InlineKeyboardMarkup(row_width=1,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(
                                             text="Конечно!",
                                             callback_data="Ok"
                                         )
                                     ]
                                 ])
