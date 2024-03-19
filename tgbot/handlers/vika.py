import asyncio

from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from loader import bot, config
from tgbot.keyboards.inline import adventure

from tgbot.keyboards.inline.FirstTaskHint.incorrect_answer1 import incorrect1
from tgbot.keyboards.inline.FirstTaskHint.incorrect_answer2 import incorrect2
from tgbot.keyboards.inline.FirstTaskHint.incorrect_answer3 import incorrect3
from tgbot.keyboards.inline.FirstTaskHint.right_answer import answer_keyboard
from tgbot.misc.states import FirstTask

incorrect_answer = 0


async def vika_start(message: Message):
    await message.answer("""Дорогая Вика, добро пожаловать в наше увлекательное приключение!🌟\n
Сегодня мы отправимся в путешествие по нашим самым важным местам, наполненным и любовью и беспечностью.💖\n
Пусть этот день станет для нас особенным, наполненным романтикой и приятными сюрпризами.\n
Готова ли ты отправиться в это незабываемое приключение со мной? 😊""",
                         reply_markup=adventure)
    await bot.send_message(chat_id=config.tg_bot.admin_ids[0], text="Она нажала на кнопку start!\nИгра началась")


async def answer_start_adventure(call: CallbackQuery):
    await call.message.answer_sticker("CAACAgIAAxkBAAO1ZfmNC6FE7TDweOlpirEXje7DzO0AAiQ_AAJVA2hIAVvZ-JnLXns0BA", )
    await asyncio.sleep(1)
    hmtl_text = "\n".join(
        ["Отлично! 😊 Теперь, чтобы начать наше приключение, давай вспомним день нашего первого знакомства",
         "Напиши мне первое сообщение, которое ты мне отправила, когда мы только познакомились.",
         "Пусть эти слова напомнят нам о нашем знакомстве и начнут наше путешествие в прошлое, наполненное беззаботностью и любовью.💕",
         "<tg-spoiler>(Да, надо ввести в бот сообщение <b>ПОЛНОСТЬЮ</b>. Не используй точки и знаки препинания. Регистр слов может быть любой)</tg-spoiler>"
         ])

    await call.message.answer(hmtl_text)
    await FirstTask.T1.set()


def register_vika(dp: Dispatcher):
    dp.register_message_handler(vika_start, commands=["start"], state="*", is_vika=True)
    dp.register_callback_query_handler(answer_start_adventure, text="Ok")
