import asyncio
import re

from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message, InputFile, ReplyKeyboardRemove

from loader import bot, config
from tgbot.keyboards.inline.ThreeTask import yes_or_no_him, yes_or_no_her, hint
from tgbot.keyboards.inline.go_four_task import go_next_four
from tgbot.misc.states import MyGift, HerGift, FindQRCode


async def three_task(call: CallbackQuery):
    await call.message.answer("Молодец, надеюсь, читая это сообщение ты выглядишь примерно так:")
    await asyncio.sleep(2)
    await call.message.answer_sticker("CAACAgIAAxkBAAIENmX57ttkLPozI-QG9ess1VCulZP9AAJpQwADNmhImZh2_rIbHeM0BA")
    await asyncio.sleep(2)
    await call.message.answer("Знаешь, меня всегда удивляла твоя способность делать подарки которые трогают до глубины души...")
    await asyncio.sleep(2)
    await call.message.answer_photo(InputFile("tgbot/photo/13.png"),
                           caption="Хотя в начале я отношения я ошибочно думал что это не так")
    await asyncio.sleep(2)
    await call.message.answer("А помнишь ли ты какой самый первый подарок ты для меня сделала?", reply_markup=yes_or_no_her)


# async def three_task(message: Message):
#     await message.answer("Молодец, надеюсь, читая это сообщение ты выглядишь примерно так:")
#     await asyncio.sleep(2)
#     await message.answer_sticker("CAACAgIAAxkBAAIENmX57ttkLPozI-QG9ess1VCulZP9AAJpQwADNmhImZh2_rIbHeM0BA")
#     await asyncio.sleep(2)
#     await message.answer(
#         "Знаешь, меня всегда удивляла твоя способность делать подарки которые трогают до глубины души...")
#     await asyncio.sleep(2)
#     await message.answer_photo(InputFile("tgbot/photo/13.png"),
#                                caption="Хотя в начале я отношения я ошибочно думал что это не так")
#     await asyncio.sleep(2)
#     await message.answer("А помнишь ли ты какой самый первый подарок ты для меня сделала?", reply_markup=yes_or_no_her)


async def yesHer(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer("И какой же?")
    await HerGift.Gift.set()


async def yesHim(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer("И какой же?)))")
    await MyGift.Gift.set()


async def noHer(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer("Тогда я напомню тебе")
    await asyncio.sleep(1)
    await call.message.answer("5 мая 2020 года началось с приятного сообщения от тебя")
    await asyncio.sleep(3)
    await call.message.answer_photo(InputFile("tgbot/photo/14.png"),
                                    caption="Даже сейчас перечитывая это сообщение мне становиться тепло на душе")
    await asyncio.sleep(4)
    await call.message.answer("И затем я получаю свой подарок!")
    await asyncio.sleep(2)
    await call.message.answer_photo(InputFile("tgbot/photo/15.png"), caption="ПОПУГИ!!!")
    await asyncio.sleep(3)
    await call.message.answer(
        "Почему-то этот момент по особенному отзывается в моем сердце, ты делала мне очень много крутых подарков, но именно этот (и еще один)"
        " запомнились мне наиболее сильно. Я хочу сказать, что благодарен тебе за этот и остальные подарки и каждый подарок для меня по особенному ценен")
    await asyncio.sleep(5)
    await call.message.answer("А помнишь ли ты какой самый первый подарок сделал для тебя я?",
                              reply_markup=yes_or_no_him)


async def noHim(call: CallbackQuery):
    await call.message.answer("Я прекрасно знаю что ты помнишь про подарок!")
    await call.message.answer("Нажми да 😡")


async def her_gift(message: Message, state: FSMContext):
    pattern = r"попуг"
    ispopug = re.search(pattern, message.text.lower())

    if (ispopug):
        await state.finish()
        await message.answer_sticker("CAACAgIAAxkBAAIF2WX7MtqeYIh1KcROlV-YS5BsvP0wAAKlGgACuNnBSrsKJnuAmUkfNAQ")
        await asyncio.sleep(1)
        await message.answer("ДА ДА ДА! Первый подарок от тебя это стикеры с попугаями!!")
        await asyncio.sleep(2)
        await message.answer_photo(InputFile("tgbot/photo/15.png"))
        await asyncio.sleep(2)
        await message.answer("А помнишь ли ты какой самый первый подарок сделал для тебя я?",
                             reply_markup=yes_or_no_him)
    else:
        await message.answer_sticker("CAACAgIAAxkBAAIF02X7MYtxGOZ7W46DwsnWHHOa5OIaAAIxIgACHZKAS2HkS2BBxiUVNAQ")
        await asyncio.sleep(1)
        await message.answer("Грустно конечно, что ты не помнишь таких базовых вещей(")


async def him_gift(message: Message, state: FSMContext):
    pattern = r"цвет|шокол|конфе"
    ispopug = re.search(pattern, message.text.lower())

    if (ispopug):
        await state.finish()
        await message.answer_sticker("CAACAgIAAxkBAAIGLWX7PXkUqB7a8s36Vr2rwn1Dv3bXAAJVHQAC2iPBSloRlSYHzNL9NAQ")
        await asyncio.sleep(1)
        await message.answer(
            "На самом деле я сам не до конца помню какой подарок я сделал первым. Либо шоколад, либо цветы на твое 20-ти летие)")
        await asyncio.sleep(2)
        await message.answer_photo(InputFile("tgbot/photo/16.jpg"))
        await asyncio.sleep(1)
        await message.answer(
            "Я до сих пор помню тот день, ту погоду и то ощущение счастья😊")

        await message.answer("Итак, чтобы продвинуться по квесту дальше, тебе нужно ввести в бота специальный код."
                             "\nПодсказку указывающую где искать код ты можешь найти в фотографиях")

        await FindQRCode.QR.set()
    else:
        await message.answer_sticker("CAACAgIAAxkBAAIGMGX7QwzYMiPrL7znL-EoLZg7fDc-AALRPAACtt9oSL0fERcJysxxNAQ")
        await asyncio.sleep(2)
        await message.answer("Мы буквально 2 дня назад говорили об этом, ты чего!?")


async def FindQr(message: Message, state: FSMContext):
    if (message.text == "54235124"):
        await state.finish()
        await message.answer_sticker("CAACAgIAAxkBAAIGxmX7T4oaCGYWlvDkJF8dBIC4_jHxAAKFHQACrRcoSHKyxcxR75g8NAQ")
        await asyncio.sleep(1)
        await message.answer("ТЫ ПРОСТО СУПЕР МОЛОЛДЕЦ!"
                             "\nНесмотря на все наши с тобой ссоры, я очень рад, что этот подарок не <s>уничтожен</s> <s>разъебан</s>"
                             "\nвыкинут, потому как спустя столько времени он по настоящему мне дорог"
                             "\nСпасибо тебе большое за него ❤️❤️❤️"
                             "\nЯ очень тебя люблю")
        await asyncio.sleep(2)
        await message.answer_sticker("CAACAgIAAxkBAAIGwGX7TxDqnHOyMNgkuVvr0Jk_ENhlAAJWHAAC18bISikDBZ-PnIX3NAQ")
        await asyncio.sleep(1)
        await message.answer_sticker("CAACAgIAAxkBAAIGw2X7T2HykxUzrau1QiZO7ECJP4rlAAJAAQACNannFC6sArI_yNPwNAQ")
        await bot.send_message(chat_id=config.tg_bot.admin_ids[0], text="Третье задание выполнено!")
        await message.answer("Твой приз ждет тебя в самой первой настолке которую мы купили!", reply_markup=go_next_four)

    else:
        await message.answer("Я могу дать тебе только одну подсказку!", reply_markup=hint)


async def hint_qr(call: CallbackQuery):
    await call.answer("Наверное из букв которые ты нашла получится какое-то слово.")
    await call.message.answer_sticker("CAACAgIAAxkBAAIGyWX7UNnqGe_Wi4R7zPCc_vsBptaZAAKlIAACcZvpSd6E9l5kST87NAQ")


def register_three_task(dp: Dispatcher):
    dp.register_callback_query_handler(three_task, text="Find second gift")
    #dp.register_message_handler(three_task, commands=["three"])
    dp.register_callback_query_handler(yesHer, text="yesHerGift")
    dp.register_callback_query_handler(noHer, text="noHerGift")
    dp.register_callback_query_handler(yesHim, text="yesHimGift")
    dp.register_callback_query_handler(noHim, text="noHimGift")
    dp.register_callback_query_handler(hint_qr, text="hintQR", state=FindQRCode.QR)
    dp.register_message_handler(her_gift, state=HerGift.Gift)
    dp.register_message_handler(him_gift, state=MyGift.Gift)
    dp.register_message_handler(FindQr, state=FindQRCode.QR)
