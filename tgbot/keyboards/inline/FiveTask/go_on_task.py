from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

she_came = InlineKeyboardMarkup(row_width=1,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(
                                             text="Я пришла",
                                             callback_data="she_came"
                                         )
                                     ]
                                 ])