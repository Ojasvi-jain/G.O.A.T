import os
import discord
from discord.ext import commands

client = commands.Bot(
    command_prefix=">",
    case_insensitive=True,
    intents=discord.Intents.all()
)
token = os.environ['DISCORD_TOKEN']
client.remove_command('help')


def start():
    cogs = ["cogs.Helpful", "cogs.Mod_Commands", "cogs.Events", "cogs.Fun"]
    print("Initialize the cogs loading process")
    for i in cogs:
        client.load_extension(i)
    print("Cogs loaded successfully \n")
    print('Active in these guilds/servers:')
    [print(g.name) for g in client.guilds]
    print('\n G.O.A.T started successfully', end="\n ------------------------ \n")
    client.run(token)


start()
