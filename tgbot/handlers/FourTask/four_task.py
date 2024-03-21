import asyncio

from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove, ContentType

from loader import config, bot
from tgbot.keyboards.inline.FourTask.WhatDoYouSee import see
from tgbot.keyboards.inline.FourTask.hints import hint1, hint2, hint3, hint4
from tgbot.keyboards.inline.go_five_task import go_next_five
from tgbot.misc.states import WhatDoYouSee, CountPhotos

count_photo = 64
HINT = 0


async def four_task(call: CallbackQuery):
    await call.message.answer("Ну чтож. Продолжим наш квест)")
    await asyncio.sleep(2)

    await call.message.answer("Первым делом тебе стоит осмотреться...")
    await asyncio.sleep(2)
    await call.message.answer("Ничего не замечаешь?", reply_markup=see)

# async def four_task(message: Message):
#     await message.answer("Ну чтож. Продолжим наш квест)")
#     await asyncio.sleep(2)
#
#     await message.answer("Первым делом тебе стоит осмотреться...")
#     await asyncio.sleep(2)
#     await message.answer("Ничего не замечаешь?", reply_markup=see)


async def similar(message: Message):
    await message.answer("И что же ты видишь?", reply_markup=ReplyKeyboardRemove())
    await WhatDoYouSee.Similar.set()


async def banan(message: Message):
    await message.answer("На самом деле ты окружена самыми ценными артефактами нашего времени."
                         "\nЭти артефакты не золото или серебро, но они – наши самые драгоценные сокровища."
                         "\nЭти маленькие прямоугольники, называемые фотографиями, хранят в себе мгновения нашей жизни. В каждом из них — море эмоций, лучи счастья и тепло наших объятий."
                         "\nНи один день не проходит, когда я не нахожу себя, вглядываясь в те тихие моменты нашего счастья."
                         "\nОни – наша тихая коллекция воспоминаний🖼️✨", reply_markup=ReplyKeyboardRemove())

    await asyncio.sleep(8)

    await message.answer(
        "Я предлагаю посчитать сколько всег/о фотографий где мы расположены, находятся у нас в квартире."
        "\nТебе стоит постараться и найти ВСЕ фотографии чтобы выполнить это задание."
        "\n<tg-spoiler>Фотографии где мы изображены отдельно тоже считаются</tg-spoiler>"
        "\n\nУдачи солнце!)😘")

    await CountPhotos.Photos.set()


async def send_creator(message: Message, state: FSMContext):
    answer = message.text
    await message.answer_sticker("CAACAgIAAxkBAAIIuGX7ZnsejUkF-uypfawBfAABV-sm3gACfhQAAl6R-Uth58UDbIVBgzQE")
    await asyncio.sleep(3)
    await message.answer("Придется все переслать моему создателю...")

    await bot.send_message(chat_id=config.tg_bot.admin_ids[0],
                           text=f"На вопрос \"что Вика видит необычного вокруг себя\", она ответила: {answer}")
    await state.finish()

    await asyncio.sleep(3)

    await message.answer("На самом деле ты окружена самыми ценными артефактами нашего времени."
                         "\nЭти артефакты не золото или серебро, но они – наши самые драгоценные сокровища."
                         "\nЭти маленькие прямоугольники, называемые фотографиями, хранят в себе мгновения нашей жизни. В каждом из них — море эмоций, лучи счастья и тепло наших объятий."
                         "\nНи один день не проходит, когда я не нахожу себя, вглядываясь в те тихие моменты нашего счастья."
                         "\nОни – наша тихая коллекция воспоминаний🖼️✨", reply_markup=ReplyKeyboardRemove())

    await asyncio.sleep(8)

    await message.answer(
        "Я предлагаю посчитать сколько всего фотографий где мы расположены, находятся у нас в квартире."
        "\nТебе стоит постараться и найти ВСЕ фотографии чтобы выполнить это задание."
        "\n<tg-spoiler>Фотографии где мы изображены отдельно тоже считаются</tg-spoiler>"
        "\n\nУдачи солнце!)😘")

    await CountPhotos.Photos.set()


async def send_count_photos(message: Message, state: FSMContext):
    global HINT
    global count_photo

    if message.text == str(count_photo):
        await state.finish()
        await message.answer_sticker("CAACAgEAAxkBAAIKG2X8BBlRHs_kituONrN9pGLk6TLxAAJ3AgAC1HTRRh3mI50THK73NAQ")
        await asyncio.sleep(2)
        await message.answer("🎉🎉🎉🎉Ты справилась с этим заданием! Поздравляю тебя.🎉🎉🎉🎉"
                             f"\nУ нас есть целых <b>{count_photo}</b> фотографии!! И у каждой есть какая-нибудь история!"
                             f"\nЯ безумно рад, что у нас с тобой есть такие ценные воспоминания!")
        await asyncio.sleep(2)
        await message.answer("И это я еще молчу про наши нераспечатанные фотографии. Я старался посчитать все наши фотки и только лишь в одном вк их оказалось больше 500."
                             "\nВ любом случае я хотел бы запечатлеть больше радостных моментов вместе с тобой ❤️")
        await asyncio.sleep(2)
        await message.answer(
            "Свой приз за выполнение этого задания ты можешь найти там, где висит фен", reply_markup=go_next_five)

        await bot.send_message(chat_id=config.tg_bot.admin_ids[0],
                               text=f"Она выполнила четвертое задание")
    elif HINT == 0:
        await message.answer("Ну я ожидал, что ты с первого раза не угадаешь", reply_markup=hint1)
        HINT += 1
    elif HINT == 1:
        await message.answer("И со второго раза не угдала???", reply_markup=hint2)
        HINT += 1
    elif HINT == 2:
        await message.answer("И с третьего раза не получилось!!??!!?!!???", reply_markup=hint3)
        HINT += 1
    elif HINT ==3:
        await message.answer("Ну вот тебе финальная подсказка чтоб уж наверняка!", reply_markup=hint4)
        HINT += 1
    else:
        await message.answer_sticker("CAACAgIAAxkBAAIJvGX8ARyVhWTraU1QngM83MBykePxAALmIwACV8MxSAbcOi79THu0NAQ")


async def hint_1(call: CallbackQuery):
    await call.message.answer("У нас есть очень классная книга приключений)")


async def hint_2(call: CallbackQuery):
    await call.message.answer("Надеюсь, ты про полноразмерные фотографии на подоконнике тоже помнишь")


async def hint_3(call: CallbackQuery):
    await call.message.answer("У меня в ящике кстати тоже есть фотографии")

async def hint_4(call: CallbackQuery):
    await call.message.answer("Не стоит забывать про нашу САМУЮ первую фотографию")

def register_four_task(dp: Dispatcher):
    #dp.register_message_handler(four_task, commands=["four"])

    dp.register_message_handler(similar, text="Да, я как раз сейчас вижу кое-что необычное🤔")
    dp.register_message_handler(banan, text="А что сказать? Ну... 🍌")

    dp.register_message_handler(send_count_photos, state=CountPhotos.Photos)
    dp.register_message_handler(send_creator, state=WhatDoYouSee.Similar)

    dp.register_callback_query_handler(hint_1, text="four_hint1", state=CountPhotos.Photos)
    dp.register_callback_query_handler(hint_2, text="four_hint2", state=CountPhotos.Photos)
    dp.register_callback_query_handler(hint_3, text="four_hint3", state=CountPhotos.Photos)
    dp.register_callback_query_handler(hint_4, text="four_hint4", state=CountPhotos.Photos)

    dp.register_callback_query_handler(four_task, text="Find three gift")
