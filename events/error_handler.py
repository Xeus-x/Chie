import discord
from discord.ext import commands

class Error_Handler(commands.Cog):
    def __init__(self, client):
        self.client = client

    # user commands
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            def convert(seconds):
                min, sec = divmod(seconds, 60)
                hour, min = divmod(min, 60)
                return "**%dh**, **%02dm**, **%02ds**" % (hour, min, sec)
            await ctx.send("Not too fast! You can use this command again in {}".format(convert(error.retry_after)))

        elif isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send("Please enter the required argument.")

        elif isinstance(error, commands.CommandNotFound):
            return None

        else:
            raise error

def setup(client):
    client.add_cog(Error_Handler(client))
