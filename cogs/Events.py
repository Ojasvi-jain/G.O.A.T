import discord
from discord.ext import commands


class events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.custom, name="Life"),
                                       status="Online")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot: return
        message.content = message.content.lower()
        if message.content == "<@!738742637993132032>":
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

            await message.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(events(bot))
