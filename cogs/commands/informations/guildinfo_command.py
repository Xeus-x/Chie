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

class GuildInfoCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["serverinfo"])
    async def guildinfo(self, ctx):
        embed = discord.Embed(
            title = ctx.guild.name + "'s Info",
            color = 0xff0000
        )
        embed.set_thumbnail(
            url = ctx.guild.icon_url
        )
        embed.add_field(
            name = "ID",
            value = ctx.guild.id,
            inline = False
        )
        embed.add_field(
            name = "Date Joined",
            value = ctx.guild.created_at.strftime("%B %d, %Y at %H:%m"),
            inline = False
        )
        embed.add_field(
            name = "Owner",
            value = ctx.guild.owner,
            inline = False
        )
        embed.add_field(
            name = "Members",
            value = ctx.guild.member_count,
            inline = True
        )
        embed.add_field(
            name = "Channels",
            value = len(ctx.guild.channels),
            inline = True
        )
        embed.add_field(
            name = "Region",
            value = ctx.guild.region,
            inline = True
        )
        embed.set_footer(
            text = ctx.author,
            icon_url = ctx.author.avatar_url
        )

        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(GuildInfoCommand(client))
