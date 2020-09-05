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

client.run(token)
