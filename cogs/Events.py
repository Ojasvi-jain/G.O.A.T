import discord
from discord.ext import commands
from random import randint
from discord.utils import get
import time
import datetime
import asyncio


class events(commands.cog):
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(events(bot))
