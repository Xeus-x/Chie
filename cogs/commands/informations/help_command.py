#   Copyright 2020-2021 Nhalrath
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import discord
from discord.ext import commands
from core import bot_info

class HelpCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            title = "Help",
            color = 0xff0000,
            url = bot_info.github
        )
        embed.add_field(
            name = "This bot is being repurposed",
            value ="The current prefix is `>`. If the prefix conflicts with the other bot's prefixes, simply remove this bot from your server.",
            inline = False
        )
        embed.set_footer(
            text = ctx.author,
            icon_url = ctx.author.avatar_url
        )

        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(HelpCommand(client))
