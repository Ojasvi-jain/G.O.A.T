import discord
from discord.ext import commands
from discord.utils import get
import time
from datetime import datetime
import asyncio


class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.teal(),
            description='The prefix of **G.O.A.T.** is \'>\''

        )

        embed.set_author(name='G.O.A.T. - Help',
                         icon_url='https://images-ext-2.discordapp.net/external/EszvAdMvtYOBEfXWbl1e2l5Vwwm3-D3uJmxRzCR38e8/%3Fsize%3D128/https/cdn.discordapp.com/icons/730302270058659950/9f7b054607cd8e9d0371be308a59699a.png')
        embed.add_field(name='Utilities :tools:',
                        value='`>help` `>ping` `>dm` `>send_dm` `>avatar` `>smoke` `>random` `>creator` `>codingame` `>krunker` `>typeracer`',
                        inline=False)
        embed.add_field(name='Moderator :oncoming_police_car:',
                        value='`>kick (disabled)` `>ban (disabled)` `>unban` `>mute` `>unmute` `>autorole` `>clear`',
                        inline=False)
        embed.add_field(name='Fun :confetti_ball:',
                        value='`>Junayed` `>Sahil` `>Murtuza` `>Tahsina` `>Itash` `>Arian` `>Faiyaz` `>Murtuza` `>Ojasvi`',
                        inline=False)

        await ctx.send(embed=embed)

    # troll
    @commands.command()
    async def muteall(self, ctx):
        await ctx.send(f"{ctx.author.mention} has muted everyone!")

    # troll
    @commands.command()
    async def unmuteall(self, ctx):
        await ctx.send(f"{ctx.author.mention} has unmuted everyone!")

    # unmute someone
    @commands.command()
    async def unmute(self, ctx, user: discord.Member):
        # await user.remove_roles(discord.utils.get(ctx.guild.roles, name="Muted")) # removes muted role
        await ctx.send(f"{user.mention} has been un-muted")
        await ctx.send(f"Sike, you thought {ctx.author.mention}")

    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def clear(self, ctx, amount=5):
        """clears chat"""
        await ctx.channel.purge(limit=amount)


def setup(bot):
    bot.add_cog(Mod(bot))
