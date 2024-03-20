from aiogram.dispatcher.filters.state import StatesGroup, State


class FirstTask(StatesGroup):
    T1 = State()


class SecondTask(StatesGroup):
    T2 = State()


class MyGift(StatesGroup):
    Gift = State()


class HerGift(StatesGroup):
    Gift = State()


class FindQRCode(StatesGroup):
    QR = State()


class WhatDoYouSee(StatesGroup):
    Similar = State()


class CountPhotos(StatesGroup):
    Photos = State()
