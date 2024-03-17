import typing

from aiogram.dispatcher.filters import BoundFilter

from tgbot.config import Config


class VikaFilter(BoundFilter):
    key = 'is_vika'

    def __init__(self, is_vika: typing.Optional[bool] = None):
        self.is_vika = is_vika

    async def check(self, obj):
        if self.is_vika is None:
            return False
        config: Config = obj.bot.get('config')
        return (obj.from_user.id == config.tg_bot.vika_id) == self.is_vika