import discord
import bot
from discord.ext import commands

class Owner(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def retrievefiles(self, ctx, password):
        if ctx.author.id == bot.owner:
            if password == bot.passw:
                await ctx.send(file = discord.File('./data/user_data.json'))
                await ctx.send(file = discord.File('./data/prefixes.json'))
            else:
                await ctx.send("You're not my master!!!")
        else:
            return False

def setup(client):
    client.add_cog(Owner(client))
