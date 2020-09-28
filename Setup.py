import discord
from discord.ext import commands
from random import randint
from discord.utils import get
import time
from datetime import datetime
import asyncio
import os

client = commands.Bot(command_prefix=">", case_insensitive=True)
token = os.getenv('DISCORD_TOKEN')
client.remove_command('help')


def start():
    cogs = ["cogs.Events", "cogs.Helpful", "cogs.Mod_Commands", "cogs.Fun"]
    print("Initialize the cogs loading process")
    for i in cogs:
        client.load_extension(i)
    print("Cogs loaded successfully")
    client.run(token)


start()
