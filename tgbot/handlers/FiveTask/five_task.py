import asyncio

from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery, InputFile

from loader import bot
from tgbot.keyboards.inline.FiveTask.go_on_task import she_came
from tgbot.keyboards.inline.FiveTask.member_photo import yes_or_no


async def five_task(call: CallbackQuery):
    chat_id = call.message.chat.id
    await call.message.answer("Ну чтож, настало время следующего задания.")
    await asyncio.sleep(2)
    await call.message.answer("Но для начала...")
    await asyncio.sleep(5)
    await call.message.answer("Мем!")
    await asyncio.sleep(1)
    ms = await call.message.answer_photo(InputFile("tgbot/photo/10.jpg"), "Бу!")
    await asyncio.sleep(2)
    await bot.delete_message(chat_id, ms.message_id)
    await asyncio.sleep(1)
    await call.message.answer("Если не успела, то сори🤷‍♂️")
    await asyncio.sleep(2)
    await call.message.answer("Вместо этого можешь еще один мем посмотреть)")
    await asyncio.sleep(2)
    await call.message.answer_photo(InputFile("tgbot/photo/17.jpg"), "Воть)")
    await asyncio.sleep(2)
    await call.message.answer("Надеюсь тебе было смешно")
    await asyncio.sleep(2)
    await call.message.answer("Ведь было же?")
    await asyncio.sleep(1)
    await call.message.answer_sticker("CAACAgIAAxkBAAIKUWX8Vs6AbeFJw1WTJ3qksHo4na14AALIGwACSukJSIJufSd74wMPNAQ")
    await asyncio.sleep(2)
    await call.message.answer("Ну ладно, приступим к нашему заданию...")
    await asyncio.sleep(2)
    await call.message.answer_photo(InputFile("tgbot/photo/18.jpg"), "Помнишь ли ты это место?", reply_markup=yes_or_no)

# async def five_task(message: Message):
#     chat_id = message.chat.id
#     await message.answer("Ну чтож, настало время следующего задания.")
#     await asyncio.sleep(2)
#     await message.answer("Но для начала...")
#     await asyncio.sleep(5)
#     await message.answer("Мем!")
#     await asyncio.sleep(1)
#     ms = await message.answer_photo(InputFile("tgbot/photo/10.jpg"), "Бу!")
#     await asyncio.sleep(2)
#     await bot.delete_message(chat_id, ms.message_id)
#     await asyncio.sleep(1)
#     await message.answer("Если не успела, то сори🤷‍♂️")
#     await asyncio.sleep(2)
#     await message.answer("Вместо этого можешь еще один мем посмотреть)")
#     await asyncio.sleep(2)
#     await message.answer_photo(InputFile("tgbot/photo/17.jpg"), "Воть)")
#     await asyncio.sleep(2)
#     await message.answer("Надеюсь тебе было смешно")
#     await asyncio.sleep(2)
#     await message.answer("Ведь было же?")
#     await asyncio.sleep(1)
#     await message.answer_sticker("CAACAgIAAxkBAAIKUWX8Vs6AbeFJw1WTJ3qksHo4na14AALIGwACSukJSIJufSd74wMPNAQ")
#     await asyncio.sleep(2)
#     await message.answer("Ну ладно, приступим к нашему заданию...")
#     await asyncio.sleep(2)
#     await message.answer_photo(InputFile("tgbot/photo/18.jpg"), "Помнишь ли ты это место?", reply_markup=yes_or_no)

async def no(call: CallbackQuery):
    await call.message.edit_reply_markup(None)
    await call.message.answer_sticker("CAACAgIAAxkBAAIKZ2X8XEoSHmtwiDZvnYH2NTr6lyvtAALUFQACq2B5Sdmgt8PAXtiZNAQ")
    await asyncio.sleep(2)
    await call.message.answer("Плохо, потому что сейчас тебе надо идти туда, чтобы выполнить очередной квест)")
    await asyncio.sleep(2)
    await call.message.answer("Как будешь на месте, тыкай на кнопочку", reply_markup=she_came)

async def yes(call:CallbackQuery):
    await call.message.edit_reply_markup(None)
    await call.message.answer("Отлично! Тогда собирайся, одевайся и выдвигайся на это место)")
    await asyncio.sleep(2)
    await call.message.answer("Как будешь на месте, тыкай на кнопочку", reply_markup=she_came)


async def she_came_to_street(call: CallbackQuery):
    await call.message.answer("Надеюсь ты добралась без происшествий!")
    await asyncio.sleep(2)
    await call.message.answer("Я считаю, что это наше самое легендарное место <tg-spoiler>(не считая машины)</tg-spoiler>"
                         "\nЗдесь я впервые увидел тебя с другой стороны. Обычно ты сдержанная и спокойная, но в этот день "
                              "я увидел в тебе хрупкую и маленькую девочку."
                         "\nВоодушевленный любовью и дофамином я помню как смотрел на тебя как на богиню которой я не достоин.")
    await asyncio.sleep(5)
    await call.message.answer_photo(InputFile("tgbot/photo/20.jpg"))
    await asyncio.sleep(2)
    await call.message.answer("Я помню как не хотел отпускать тебя и желал держать тебя в своих руках бесконечно!")
    await asyncio.sleep(3)
    await call.message.answer_photo(InputFile("tgbot/photo/21.jpg"))
    await asyncio.sleep(2)
    await call.message.answer("Я помню как не хотел уходить от тебя на работу, учебу, домой, к друзьям,!")
    await asyncio.sleep(3)
    await call.message.answer_photo(InputFile("tgbot/photo/22.png"))
    await asyncio.sleep(2)
    await call.message.answer("Помню как мы начали перекидываться милыми картинками и в последствии видосами")
    await asyncio.sleep(3)
    await call.message.answer_photo(InputFile("tgbot/photo/23.jpg"))
    await asyncio.sleep(2)
    await call.message.answer("Я помню все и невероятно ценю те моменты, потому как помню, что мы оба были окрыленны любовью и "
                              "никогда не хотели расставаться.")
    await asyncio.sleep(2)
    await call.message.answer("Хочу сказать, что я очень люблю тебя и несмотря на все проблемы и трудности которые есть "
                              "в наших отношениях, я безмерно счастлив быть с тобой, обнимать тебя, смеяться с тобой, проживать и худшие, и лучшие моменты моей жизни. "
                              "Спасибо тебе за все!")
    await asyncio.sleep(2)
    await call.message.answer("Я очень сильно тебя люблю❤️")
    await asyncio.sleep(60)
    await call.message.answer(".")
    await asyncio.sleep(2)
    await call.message.answer(".")
    await asyncio.sleep(2)
    await call.message.answer(".")
    await asyncio.sleep(2)
    await call.message.answer(".")
    await asyncio.sleep(2)
    await call.message.answer(".")
    await asyncio.sleep(2)
    await call.message.answer(".")
    await asyncio.sleep(2)
    await call.message.answer(".")
    await asyncio.sleep(2)
    await call.message.answer(".")
    await asyncio.sleep(2)
    await call.message.answer(".")
    await asyncio.sleep(2)
    await call.message.answer(".")
    await asyncio.sleep(2)
    await call.message.answer(".")
    await asyncio.sleep(2)
    await call.message.answer(".")
    await asyncio.sleep(2)
    await call.message.answer(".")
    await asyncio.sleep(2)
    await call.message.answer(".")
    await asyncio.sleep(2)
    await call.message.answer(".")
    await asyncio.sleep(2)
    await call.message.answer("Продолжение следует...😉")



def register_five_task(dp: Dispatcher):
    #dp.register_message_handler(five_task, commands=["five"])

    dp.register_callback_query_handler(yes, text="yesPhoto")
    dp.register_callback_query_handler(no, text="noPhoto")

    dp.register_callback_query_handler(she_came_to_street, text="she_came")

    dp.register_callback_query_handler(five_task, text="Find four gift")