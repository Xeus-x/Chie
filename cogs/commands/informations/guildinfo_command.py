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

class GuildInfoCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["serverinfo"])
    async def guildinfo(self, ctx):
        embed = discord.Embed(
            title = ctx.guild.name + "'s Info",
            color = 0xff0000
        ).set_thumbnail(
            url = ctx.guild.icon_url
        ).add_field(
            name = "ID",
            value = ctx.guild.id,
            inline = False
        ).add_field(
            name = "Date Created",
            value = ctx.guild.created_at.strftime("%B %d, %Y at %H:%m"),
            inline = False
        ).add_field(
            name = "Owner",
            value = ctx.guild.owner,
            inline = False
        ).add_field(
            name = "Members",
            value = ctx.guild.member_count,
            inline = True
        ).add_field(
            name = "Channels",
            value = len(ctx.guild.channels),
            inline = True
        ).add_field(
            name = "Region",
            value = ctx.guild.region,
            inline = True
        ).set_footer(
            text = ctx.author,
            icon_url = ctx.author.avatar_url
        )

        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(GuildInfoCommand(client))
