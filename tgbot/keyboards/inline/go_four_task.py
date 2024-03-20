from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

go_next_four = InlineKeyboardMarkup(row_width=1,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(
                                             text="Нашла!",
                                             callback_data="Find three gift"
                                         )
                                     ]
                                 ])
