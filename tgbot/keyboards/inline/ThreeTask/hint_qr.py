from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

hint = InlineKeyboardMarkup(row_width=1,
                            inline_keyboard=[
                                [
                                    InlineKeyboardButton(
                                        text="Подсказка",
                                        callback_data="hintQR"
                                    )
                                ]
                            ])
