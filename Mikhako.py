import os

from decouple import config
from discord.ext import commands


class Mikakho_bot(commands.Bot):
    def __init__(self, command_prefix, self_bot):
        super().__init__(command_prefix=command_prefix, self_bot=self_bot)
        self.load_cogs()

    def load_cogs(self):
        for filename in os.listdir("./Cogs"):
            if filename.endswith(".py"):
                self.load_extension(f"Cogs.{filename[:-3]}")


Bot = Mikakho_bot(command_prefix=config("COMMAND_PREFIX", default="-"), self_bot=False)
Bot.run(config("BOT_TOKEN"))
