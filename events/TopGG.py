import dbl
import bot
import discord
from discord.ext import commands

class TopGG(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.token = bot.tggToken
        self.dblpy = dbl.DBLClient(self.client, self.token, autopost=True)

    @commands.Cog.listener()
    async def on_guild_post(self):
        print("Server count posted successfully")

def setup(client):
    client.add_cog(TopGG(client))
