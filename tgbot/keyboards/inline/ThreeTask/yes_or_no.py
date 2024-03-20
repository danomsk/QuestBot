from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

yes_or_no_him = InlineKeyboardMarkup(row_width=1,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(
                                             text="Да",
                                             callback_data="yesHimGift"
                                         ),
                                        InlineKeyboardButton(
                                             text="Нет",
                                             callback_data="noHimGift"
                                         ),
                                     ]
                                 ])

yes_or_no_her = InlineKeyboardMarkup(row_width=1,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(
                                             text="Да",
                                             callback_data="yesHerGift"
                                         ),
                                        InlineKeyboardButton(
                                             text="Нет",
                                             callback_data="noHerGift"
                                         ),
                                     ]
                                 ])
