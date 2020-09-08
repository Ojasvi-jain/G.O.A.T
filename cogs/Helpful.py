import discord
from discord.ext import commands
from random import randint
from discord.utils import get
import time
from datetime import datetime
import asyncio


class Helpful(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def role_info(self, ctx, role: discord.Role) -> None:
        """this fuction returns the names of all the member with that role."""
        embed = discord.Embed(
            title=f"List of people with the role {role.name}:[Total members with the role:[{len(role.members)}]"
            , color=role.color)

        for member in role.members:
            embed.add_field(name="~~~~~~~~~~~~~~~~~"
                            , value=f"{member.name}")

        await ctx.send(embed=embed)

    @commands.command()
    async def avatar(self, ctx, member: discord.Member):
        show_avatar = discord.Embed(

            colour=discord.Colour.teal()
        )
        show_avatar.set_image(url='{}'.format(member.avatar_url))
        await ctx.send(embed=show_avatar)


def setup(bot):
    bot.add_cog(Helpful(bot))
