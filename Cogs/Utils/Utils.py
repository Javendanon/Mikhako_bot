import discord
from discord.ext import commands


class Utils(commands.Cog):
    def __init___(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed()
        embed.title = ":ping_pong: Pong! la reconchadetumadre"
        embed.colour = 0x0000ff
        embed.description = "testing_message"
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_ready(self):
        print("Mikhako-bot cumbiero listening.")


def setup(bot):
    bot.add_cog(Utils(bot))