import datetime
import discord
from discord.ext import commands


class Helpful(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def role_info(self, ctx, role: discord.Role) -> None:
        """this function returns the names of all the member with that role."""
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

    @commands.command()
    async def send_dm(self, ctx, member: discord.Member, *content):
        channel = await member.create_dm()
        await channel.send(f"{' '.join(content)} \n ----------------------------  \n " 
                           f"Getting a message from bot never gets old;)")


def setup(bot):
    bot.add_cog(Helpful(bot))
