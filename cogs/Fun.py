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
    async def spam(self, ctx, member: discord.Member, amount=7, *,
                   content="How does it feel to get spammed"):
        print(ctx)
        await ctx.channel.purge(limit=1)
        for i in range(int(amount)):
            await (ctx.send(f"--__-- :rofl: {member.mention}, {content}"))
        print("Just spammed people!lol")

    @commands.command()
    async def no_bs(self, ctx):
        await ctx.send(f"This is a peaceful server ☮ we don't want any kind of bs in here,\n \
If u are willing to fight go to either Dm's or in channel <#753067495686144123> \n Thank You for your corporation ✌")


def setup(bot):
    bot.add_cog(Fun(bot))
