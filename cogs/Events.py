import discord
from discord.ext import commands


class events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Life"),
                                       status="Online")

    @commands.Cog.listener()
    async def on_message(self, message):
        message.content = message.content.lower()
        if message.author.bot:
            return None
        else:
            if message.content == "<@!765457803673337876>":
                await message.channel.send("Type `>help ` for more info")

            if message.guild is None and not message.author.bot:
                channel = self.bot.get_channel(765861714817843221)
                await channel.send(f"Author: ``{message.author}`` \nReply: ``{message.content}`` \n----------------")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f"Welcome {member}")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """
        The event triggered when an error is raised while invoking a command.
        Parameters
        ------------
        ctx: commands.Context
            The context used for command invocation.
        error: commands.CommandError
            The Exception raised.
        """
        # This prevents any commands with local handlers being handled here in on_command_error.
        if hasattr(ctx.command, 'on_error'):
            return

        # This prevents any cogs with an overwritten cog_command_error being handled here.
        cog = ctx.cog
        if cog:
            if cog._get_overridden_method(cog.cog_command_error) is not None:
                return
        # Allows us to check for original exceptions raised and sent to CommandInvokeError.
        # If nothing is found. We keep the exception passed to on_command_error.
        error = getattr(error, 'original', error)

        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Wake up there is no such command ")

        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(" :rofl: U don't have the Perms to execute the command")

        elif isinstance(error, commands.DisabledCommand):
            await ctx.send(f'{ctx.command} has been disabled.')

        elif isinstance(error, commands.MemberNotFound):
            await ctx.send("I could not find that member. Please try again.")

        elif isinstance(error, commands.NoPrivateMessage):
            try:
                await ctx.author.send(f'{ctx.command} can not be used in Private Messages.')
            except discord.HTTPException:
                pass

        # For this error example we check to see where it came from...
        elif isinstance(error, commands.BadArgument):
            await ctx.send('I could not find that member. Please try again.')

        else:
            # All other Errors    not returned come here. And we can just print the default TraceBack.
            print(f"Ignoring exception in command {ctx.command}: ")


def setup(bot):
    bot.add_cog(events(bot))
