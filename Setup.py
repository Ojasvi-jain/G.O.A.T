import discord
from discord.ext import commands
from random import randint
from discord.utils import get
import time
from datetime import datetime
import asyncio
import os

client = commands.Bot(command_prefix=">")
token = os.getenv('DISCORD_TOKEN')


def start():
    print("Initialize the cogs loading process")
    client.load_extension("cogs.Fun")
    client.load_extension("cogs.Mod_Commands")
    client.load_extension("cogs.Helpful")
    print("Cogs loaded successfully")
    client.run(token)


start()
