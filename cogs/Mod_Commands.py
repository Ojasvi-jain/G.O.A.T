import discord
from discord.ext import commands
import time


class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.initial_time = time.monotonic()

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

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="No Reason!"):
        await ctx.send(f'Nice try {ctx.author.mention}!')

        if member == None or member == ctx.message.author:
            await ctx.channel.send("You cannot kick yourself!")
            return
        await member.kick(reason=reason)
        await ctx.send(f'Kicked {member}!')

    @commands.command()
    async def ping(self, ctx):
        current_uptime = round(time.monotonic() - self.initial_time, 2)
        embed = discord.Embed(
            title="G.O.A.T", description="Ping Details", color=0xc41c1c)
        embed.set_thumbnail(
            url="https://lever-client-logos.s3-us-west-2.amazonaws.com/2034f09a-3588-4411-8f4a-26e0da70d11a-1590002495817.png")
        embed.add_field(name="🏓 Ping ", value=str(f"Pong! **{round(self.bot.latency * 1000)} ms**."), inline=False)
        embed.add_field(name="👍 Uptime",
                        value=str(time.strftime("%H: %M: %S", time.gmtime(current_uptime))) + "s", inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Mod(bot))
