import asyncio

from PIL import Image, ImageChops
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, InputFile, CallbackQuery, MediaGroup, ContentType

from loader import config, bot
from tgbot.keyboards.inline.go_three_task import go_next_three
from tgbot.misc.states import SecondTask


# async def second_task(message: Message):
#     time_sleep = 2
#     await message.answer("Пока ты кушаешь киндер, я уже приготовил для тебя второе задание)))\n\n"
#                          "Итак, вернемся к началу нашего знакомства. Я помню, что мы очень быстро стали присылать друг-другу мемный фотки)"
#                          "\nИ вот некоторые из них...")
#
#     await asyncio.sleep(time_sleep)
#     await message.answer_photo(photo=InputFile(path_or_bytesio="tgbot/photo/1.jpg"),
#                                caption="Это я получил когда мы впервые начали говорить на запретные темы"
#                                        "\n<tg-spoiler><b>Я ПРО SEX</b></tg-spoiler>")
#     await asyncio.sleep(time_sleep-2)
#     await message.answer_photo(photo=InputFile(path_or_bytesio="tgbot/photo/2.jpg"),
#                                caption="А эту фотографию ты мне отправила, когда говорила что хочешь футболку с таким принтом)")
#
#     await asyncio.sleep(time_sleep-2)
#     await message.answer_photo(photo=InputFile(path_or_bytesio="tgbot/photo/5.jpg"),
#                                caption="Тут ты очень смешнявая))")
#
#     await asyncio.sleep(time_sleep-2)
#     await message.answer_photo(photo=InputFile(path_or_bytesio="tgbot/photo/3.jpg"),
#                                caption="А тут я очень смешной)")
#
#     await asyncio.sleep(time_sleep-2)
#     album = MediaGroup()
#     album.attach_photo(InputFile(path_or_bytesio="tgbot/photo/4(2).jpg"), caption="А здесь я стараюсь повторить твои движения))🥰")
#     album.attach_photo(InputFile(path_or_bytesio="tgbot/photo/4(1).jpg"))
#     await message.answer_media_group(media=album)
#
#     await asyncio.sleep(time_sleep-2)
#     await message.answer_photo(photo=InputFile(path_or_bytesio="tgbot/photo/7.jpg"),
#                                caption="Это я оставлю без комментариев")
#
#     await asyncio.sleep(time_sleep-2)
#     await message.answer_photo(photo=InputFile(path_or_bytesio="tgbot/photo/8.jpg"),
#                                caption="Тут ты очень мило спишь😍")
#
#     await asyncio.sleep(time_sleep-2)
#     await message.answer_photo(photo=InputFile(path_or_bytesio="tgbot/photo/11.jpg"),
#                                caption="А здесь не очень мило сплю я🤡")
#
#     await asyncio.sleep(time_sleep-2)
#     await message.answer("К сожалению я не могу запихать в этот квест ВСЕ наши фотографии, иначе квест никогда не закончится, но пролистывая наши фотографии"
#                          " в самом начале отношений я словил огромную дозу кайфа и надеюсь, что ты тоже."
#                          "\nКстати.."
#                          "\nРаз уж мы заговорили о фотографиях, то вот тебе следующее задание:"
#                          "\n\n<b>Тебе надо найти самую первую фотографию отправленную мне, на которой ты изображена во всей красе, и отправить ее сюда.</b>"
#                          "\n\nУдачи!")
#
#     await SecondTask.T2.set()


async def second_task(call: CallbackQuery):
    time_sleep = 5
    await call.message.answer("Пока ты кушаешь киндер, я уже приготовил для тебя второе задание)))\n\n"
                         "Итак, вернемся к началу нашего знакомства. Я помню, что мы очень быстро стали присылать друг-другу мемный фотки)"
                         "\nИ вот некоторые из них...")

    await asyncio.sleep(time_sleep)
    await call.message.answer_photo(photo=InputFile(path_or_bytesio="tgbot/photo/1.jpg"),
                               caption="Это я получил когда мы впервые начали говорить на запретные темы"
                                       "\n<tg-spoiler><b>Я ПРО SEX</b></tg-spoiler>")
    await asyncio.sleep(time_sleep-2)
    await call.message.answer_photo(photo=InputFile(path_or_bytesio="tgbot/photo/2.jpg"),
                               caption="А эту фотографию ты мне отправила, когда говорила что хочешь футболку с таким принтом)")

    await asyncio.sleep(time_sleep-2)
    await call.message.answer_photo(photo=InputFile(path_or_bytesio="tgbot/photo/5.jpg"),
                               caption="Тут ты очень смешнявая))")

    await asyncio.sleep(time_sleep-2)
    await call.message.answer_photo(photo=InputFile(path_or_bytesio="tgbot/photo/3.jpg"),
                               caption="А тут я очень смешной)")

    await asyncio.sleep(time_sleep-2)
    album = MediaGroup()
    album.attach_photo(InputFile(path_or_bytesio="tgbot/photo/4(2).jpg"), caption="А здесь я стараюсь повторить твои движения))🥰")
    album.attach_photo(InputFile(path_or_bytesio="tgbot/photo/4(1).jpg"))
    await call.message.answer_media_group(media=album)

    await asyncio.sleep(time_sleep-2)
    await call.message.answer_photo(photo=InputFile(path_or_bytesio="tgbot/photo/7.jpg"),
                               caption="Это я оставлю без комментариев")

    await asyncio.sleep(time_sleep-2)
    await call.message.answer_photo(photo=InputFile(path_or_bytesio="tgbot/photo/8.jpg"),
                               caption="Тут ты очень мило спишь😍")

    await asyncio.sleep(time_sleep-2)
    await call.message.answer_photo(photo=InputFile(path_or_bytesio="tgbot/photo/11.jpg"),
                               caption="А здесь не очень мило сплю я🤡")

    await asyncio.sleep(time_sleep-2)
    await call.message.answer("К сожалению я не могу запихать в этот квест ВСЕ наши фотографии, иначе квест никогда не закончится, но пролистывая наши фотографии"
                         " в самом начале отношений я словил огромную дозу кайфа и надеюсь, что ты тоже."
                         "\nКстати.."
                         "\nРаз уж мы заговорили о фотографиях, то вот тебе следующее задание:"
                         "\n\n<b>Тебе надо найти самую первую фотографию отправленную мне, на которой ты изображена во всей красе, и отправить ее сюда.</b>"
                         "\n\nУдачи!")

    await SecondTask.T2.set()

async def answer_photo(message: Message, state: FSMContext):
    img1 = "tgbot/photo/12.png"
    await message.photo[-1].download(destination_file="tgbot/photo/test.png")
    img2 = "tgbot/photo/test.png"
    if(await difference_images(img1, img2)):
        await message.answer_sticker("CAACAgIAAxkBAAIDM2X525GnmhFeCGd2OFInCYRgN8fWAALJRgACdllhSLXuF_MYz_oWNAQ")
        await asyncio.sleep(1)
        await message.answer("Поздравляю! Но думаю это было простое задание. Дальше будет сложнее)\n"
                             "Твой приз ждет тебя в ящике кровати 🎉", reply_markup=go_next_three)
        await state.finish()
        await bot.send_message(chat_id=config.tg_bot.admin_ids[0], text="Второе задание выполнено!")
    else:
        await message.answer("Это не та фотография. Поищи еще\n"
                             "<tg-spoiler>На мой взгляд это простое задание, так что подсказок не будет</tg-spoiler>")


async def difference_images(img1, img2):
    image1 = Image.open(img1)
    image2 = Image.open(img2)

    result = ImageChops.difference(image1, image2)
    if result.getbbox() == None:
        print(img1, img2, 'matches')
        return True
    else:
        result.save("result.jpg")
        return False

async def echo_answer_text(message:Message):
    await message.answer("Наверно логично, что боту нужно отправлять фотографию, а не текст")
    await message.answer_sticker("CAACAgIAAxkBAAIDRGX53UCb0d4HQJV1cy2xim5TE-3NAAIwQAACRUNhSEmBR7w4Xi8wNAQ")

async def echo_answer_document(message:Message):
    await message.answer_sticker("CAACAgIAAxkBAAIDRGX53UCb0d4HQJV1cy2xim5TE-3NAAIwQAACRUNhSEmBR7w4Xi8wNAQ")
    await message.answer("Не отправляй сжатое изображение")


def register_second_task(dp: Dispatcher):
    dp.register_callback_query_handler(second_task, text="Find first gift")
    #dp.register_message_handler(second_task, commands=["second"])
    dp.register_message_handler(answer_photo, state=SecondTask.T2, content_types=ContentType.PHOTO)
    dp.register_message_handler(echo_answer_text, state=SecondTask.T2, content_types=ContentType.TEXT)
    dp.register_message_handler(echo_answer_document, state=SecondTask.T2, content_types=ContentType.DOCUMENT)
