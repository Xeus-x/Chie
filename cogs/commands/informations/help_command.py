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
import json
from discord.ext import commands
from core import bot_info

class HelpCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    async def check(self):
        with open('./cogs/commands/informations/help.json', 'r') as f:
            data = json.load(f)
        return data

    @commands.command()
    async def help(self, ctx, page=None):
        if page == None:
            embed = discord.Embed(
                title = "Help",
                color = 0xff0000,
                url = bot_info.github
            )
            embed.add_field(
                name = "Miscellaneous",
                value = "`choose`, `dice`, `ping`, `say`",
                inline = False
            )
            embed.add_field(
                name = "Informations",
                value = "`guildinfo`, `userinfo`, `help`",
                inline = False 
            )
            embed.add_field(
                name = "Images",
                value = "`danbooru`, `safebooru`, `hug`, `slap`, `kiss`",
                inline = False
            )
            embed.set_footer(
                text = ctx.author,
                icon_url = ctx.author.avatar_url
            )

            await ctx.send(embed = embed)
        else:
            data = await self.check()
            if str(page) in data:
                smpl = data[str(page)]

                embed = discord.Embed(
                    title = page,
                    color = 0xff0000,
                )
                embed.add_field(
                    name = "Aliases",
                    value = smpl["alias"],
                    inline = False
                )
                embed.add_field(
                    name = "Usage",
                    value = smpl["usage"],
                    inline = False
                )
                embed.add_field(
                    name = "Description",
                    value = smpl["description"],
                    inline = False
                )
                embed.set_footer(
                    text = ctx.author,
                    icon_url = ctx.author.avatar_url
                )

                await ctx.send(embed = embed)

            else:
                await ctx.send("**What's this? I've never heard of this command before...**")

def setup(client):
    client.add_cog(HelpCommand(client))
