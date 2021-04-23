from discord.ext.commands import Bot, Context


class CommandBuilder(commands.bot):
    def __init__(self, Bot, Context, kind):
        self.bot = Bot
        self.context = Context
        self.kind = kind
