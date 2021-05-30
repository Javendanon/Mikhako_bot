import os
import re

from decouple import config
from discord.ext import commands


class Settings(commands.Bot):
    def __init__(self, command_prefix, self_bot):
        self._name = "GatoQQ"
        self._profile_img = "https://pbs.twimg.com/profile_images/1189898699629060096/6XkNuOMK_400x400.jpg"
        super().__init__(command_prefix=command_prefix, self_bot=self_bot)

    @property
    def name(self):
        return self._name

    @property
    def profile_img(self):
        return self._profile_img

    @name.setter
    def name(self, name):
        self._name = name

    @profile_img.setter
    def profile_img(self, img_url):
        self._profile_img = img_url


class Mikakho_bot(Settings):
    def __init__(self, command_prefix, self_bot):
        super().__init__(command_prefix=command_prefix, self_bot=self_bot)
        self.load_cogs()

    def load_cogs(self):
        for subdir, dirs, files in os.walk("./Cogs"):
            for filename in files:
                if filename.endswith(".py"):
                    directory = re.sub("(?:(\W|(?:php|html)))", ".", subdir)
                    self.load_extension(f"{directory[2:]}.{filename[:-3]}")


Bot = Mikakho_bot(command_prefix=config("COMMAND_PREFIX", default="-"), self_bot=False)
Bot.run(config("BOT_TOKEN"))
