import asyncio

from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from loader import bot, config

from tgbot.keyboards.inline.FirstTaskHint.incorrect_answer1 import incorrect1
from tgbot.keyboards.inline.FirstTaskHint.incorrect_answer2 import incorrect2
from tgbot.keyboards.inline.FirstTaskHint.incorrect_answer3 import incorrect3
from tgbot.keyboards.inline.FirstTaskHint.right_answer import answer_keyboard
from tgbot.keyboards.inline.go_second_task import go_next_second
from tgbot.misc.states import FirstTask

incorrect_answer = 0

async def answer_t1(message: Message, state: FSMContext):
    global incorrect_answer
    answer = message.text
    right_ansewer = ("ну я зашла в друзья к лере банщиковой ввела твое имя там тебя не было я зашла к яне звягинцевой "
                     "потому что знаю то что она была до 11 класса вроде бы как вот ну то-есть она точно должна "
                     "тебя знать и все и нашла там вот такая я я же девушка ты что я же умею")

    if (answer.lower() == right_ansewer):
        await message.answer("Надеюсь для тебя это было не слишком сложно)"
                             "\n\nПомню как сидел и общался с тобой, и даже подумать не могу насколько далеко зайдет наша с тобой история."
                             "\n\nКстати, так как у нас квест, то тебе полагается награда за выполение первого задания."
                             "\nТвой приз ждет тебя  под кухонным столом!", reply_markup=go_next_second)
        await bot.send_message(chat_id=config.tg_bot.admin_ids[0], text="Первое задание выполнено!")
        await state.finish()
    elif (incorrect_answer == 0):
        await message.answer("Попробуй еще раз", reply_markup=incorrect1)
        incorrect_answer += 1
    elif (incorrect_answer == 1):
        await message.answer("Снова не вышло, попробуй еще разок", reply_markup=incorrect2)
        incorrect_answer += 1
    elif (incorrect_answer == 2):
        await message.answer("Ну все, последняя подсказка!", reply_markup=incorrect3)
        incorrect_answer += 1
    else:
        await message.answer("Ну чтож ты так, там же все просто", reply_markup=answer_keyboard)


async def hint1(call: CallbackQuery):
    await call.answer(text="Смешки в голосовом прописывать не надо 😎")


async def hint2(call: CallbackQuery):
    await call.answer(text="Число одиннадцать лучше вводить числом 😎")


async def hint3(call: CallbackQuery):
    await call.answer(
        text="Первая часть ответа: ну я зашла в друзья к лере банщиковой ввела твое имя там тебя не было я зашла к яне звягинцевой")


async def answer(call: CallbackQuery):
    await call.answer(text="Вторая часть ответа: потому что знаю то что она была до 11 класса вроде бы как вот ну то-есть она точно должна "
                      "тебя знать и все и нашла там вот такая я я же девушка ты что я же умею")


def register_first_task(dp: Dispatcher):
    dp.register_message_handler(answer_t1, state=FirstTask.T1)

    dp.register_callback_query_handler(hint1, text="Hint1", state=FirstTask.T1)
    dp.register_callback_query_handler(hint2, text="Hint2", state=FirstTask.T1)
    dp.register_callback_query_handler(hint3, text="Hint3", state=FirstTask.T1)
    dp.register_callback_query_handler(answer, text="answer", state=FirstTask.T1)