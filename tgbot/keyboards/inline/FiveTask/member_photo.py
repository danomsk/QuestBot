from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

yes_or_no = InlineKeyboardMarkup(row_width=1,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(
                                             text="Да",
                                             callback_data="yesPhoto"
                                         ),
                                        InlineKeyboardButton(
                                             text="Нет",
                                             callback_data="noPhoto"
                                         ),
                                     ]
                                 ])