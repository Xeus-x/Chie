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

class UserInfoCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["profile"])
    async def userinfo(self, ctx, mention:discord.Member=None):
        def embedBuilder(user):
            embed = discord.Embed(
                title = user.name + "'s Profile",
                color = 0xff0000
            )
            embed.set_thumbnail(
                url = user.avatar_url
            )
            embed.add_field(
                name = "ID",
                value = user.id,
                inline = False
            )
            embed.add_field(
                name = "Date Created",
                value = user.created_at.strftime("%B %d, %Y at %H:%m"),
                inline = False
            )
            embed.set_footer(
                text = ctx.author,
                icon_url = ctx.author.avatar_url
            )

            return embed
        
        if mention == None:
            embed = embedBuilder(ctx.author)
        else:
            embed = embedBuilder(mention)

        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(UserInfoCommand(client))
