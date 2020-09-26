import discord
from discord.ext import commands
import random
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

    @commands.command()
    async def say(self, ctx, member: discord.Member, *, msg="U suck"):
        """
       Make webhooks which imitate actual person.
        """
        webhook = await ctx.channel.create_webhook(name="su")
        await webhook.send(content=msg, username=member.name, avatar_url=member.avatar_url)
        await webhook.delete()

    @commands.command()
    async def smoke(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour(0x006400),
            title='SmokerOP',
            description='You smoked too much weed with Murtuza, and **you fell on roof While dancing!**'
        )

        embed.set_image(url="https://media.giphy.com/media/Tglfor5oAY4icwI5X2/giphy.gif")
        embed.set_footer(text="Made with Smoke! | Don't Smoke Weed ⚰ everyday")

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Fun(bot))
