import discord
from discord.ext import commands
from random import randint
from discord.utils import get
import time
from datetime import datetime
import asyncio


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def no_bs(self, ctx):
        await ctx.send(f"This is a peaceful server ☮ we don't want any kind of bs in here,\n \
If u are willing to fight go to either Dm's or in channel <#753067495686144123> \n Thank You for your corporation ✌")


def setup(bot):
    bot.add_cog(Fun(bot))
