import discord
from discord.ext import commands


class events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.custom, name="Life"),
                                       status="Online")


def setup(bot):
    bot.add_cog(events(bot))
