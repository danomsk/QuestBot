from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

hint1 = InlineKeyboardMarkup(row_width=1,
                             inline_keyboard=[
                                 [
                                     InlineKeyboardButton(
                                         text="1 Подсказка",
                                         callback_data="four_hint1"
                                     )
                                 ]
                             ])

hint2 = InlineKeyboardMarkup(row_width=1,
                             inline_keyboard=[
                                 [
                                     InlineKeyboardButton(
                                         text="2 Подсказка",
                                         callback_data="four_hint2"
                                     )
                                 ]
                             ])

hint3 = InlineKeyboardMarkup(row_width=1,
                             inline_keyboard=[
                                 [
                                     InlineKeyboardButton(
                                         text="3 Подсказка",
                                         callback_data="four_hint3"
                                     )
                                 ]
                             ])

hint4 = InlineKeyboardMarkup(row_width=1,
                             inline_keyboard=[
                                 [
                                     InlineKeyboardButton(
                                         text="4 Подсказка",
                                         callback_data="four_hint4"
                                     )
                                 ]
                             ])