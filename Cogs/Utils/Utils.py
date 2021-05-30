import discord
from discord.ext import commands


class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        latency = (self.bot.latency) * 1000
        embed = discord.Embed(
            title=":ping_pong: Pong!",
            colour=0x0000ff,
            description=f"{self.bot.name} says: La latencia es de {round(latency,2)} ms",
        )
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_ready(self):
        print("GatoQQ listening.")


def setup(bot):
    bot.add_cog(Utils(bot))