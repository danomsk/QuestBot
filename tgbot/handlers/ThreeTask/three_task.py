import asyncio

from aiogram import Dispatcher
from aiogram.types import CallbackQuery, Message, InputFile, ReplyKeyboardRemove

from tgbot.keyboards import yes_or_no


# async def three_task(call: CallbackQuery):
#     await call.message.answer("Молодец, надеюсь, читая это сообщение ты выглядишь примерно так:")
#     await asyncio.sleep(1)
#     await call.message.answer_sticker("CAACAgIAAxkBAAIENmX57ttkLPozI-QG9ess1VCulZP9AAJpQwADNmhImZh2_rIbHeM0BA")
#     await asyncio.sleep(1)
#     await call.message.answer("Знаешь, меня всегда удивляла твоя способность делать подарки которые трогают до глубины души...")
#     await call.message.answer("А помнишь ли ты какой самый первый подарок ты для меня сделала?", reply_markup=yes_or_no)

async def three_task(message: Message):
    await message.answer("Молодец, надеюсь, читая это сообщение ты выглядишь примерно так:")
    await asyncio.sleep(1)
    await message.answer_sticker("CAACAgIAAxkBAAIENmX57ttkLPozI-QG9ess1VCulZP9AAJpQwADNmhImZh2_rIbHeM0BA")
    await asyncio.sleep(1)
    await message.answer("Знаешь, меня всегда удивляла твоя способность делать подарки которые трогают до глубины души...")
    await message.answer_photo(InputFile("tgbot/photo/13.png"), caption="Хотя в начале я отношения я ошибочно думал что это не так")
    await message.answer("А помнишь ли ты какой самый первый подарок ты для меня сделала?", reply_markup=yes_or_no)

async def yes(message: Message):
    await message.answer("И какой же?")

async def no(message: Message):
    await message.answer("Тогда я напомню тебе", reply_markup=ReplyKeyboardRemove())
    await asyncio.sleep(1)
    await message.answer("5 мая 2020 года началось с приятного сообщения от тебя")
    await asyncio.sleep(3)
    await message.answer_photo(InputFile("tgbot/photo/14.png"), caption="Даже сейчас перечитывая это сообщение мне становиться тепло на душе")
    await asyncio.sleep(4)
    await message.answer("И затем я получаю свой подарок!")
    await asyncio.sleep(2)
    await message.answer_photo(InputFile("tgbot/photo/15.png"), caption="ПОПУГИ!!!")
    await asyncio.sleep(3)
    await message.answer("Почему-то этот момент по особенному отзывается в моем сердце, ты делала мне очень много крутых подарков, но именно этот (и еще один)"
                         " запомнились мне наиболее сильно. Я хочу сказать, что благодарен тебе за этот и остальные подарки и каждый подарок для меня по особенному ценен")
    await asyncio.sleep(5)
    await message.answer("А помнишь ли ты какой самый первый подарок сделал для тебя я?")

def register_three_task(dp: Dispatcher):
    #dp.register_callback_query_handler(three_task, text="Find second gift")
    dp.register_message_handler(three_task, commands=["three"])
    dp.register_message_handler(yes, text="Да")
    dp.register_message_handler(no, text="Нет")
