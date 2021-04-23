import os
import re

from decouple import config
from discord.ext import commands


class Mikakho_bot(commands.Bot):
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
