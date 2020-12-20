#   Copyright 2020 Nhalrath
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
from datetime import datetime
from discord.ext import commands

guild_id = "Guild ID"
log_id = """Logs Channel ID"""

class Forum_Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    # When member joins the Forum.
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.client.get_channel("""Channel ID""")
        guild = self.client.get_guild(guild_id)
        log = self.client.get_channel(log_id)

        if member.guild == guild:
            role = discord.utils.get(member.guild.roles, name = "Member")
            await member.add_roles(role)
            await channel.send(f"Welcome to the guild, {member.mention}!")
            await log.send(f"```{datetime.now()} | {member.mention} joined!```")
        else:
            return False

    # When the member leaves the forum.
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        guild = self.client.get_guild(guild_id)
        log = self.client.get_channel(log_id)
        if member.guild == guild:
            await log.send(f"```{datetime.now()} | {member.mention} left!```")
        else:
            return False

    # When a message is edited
    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        guild = self.client.get_guild(guild_id)
        log = self.client.get_channel(log_id)

        if before.author == self.client.user:
            return False
        elif before.guild == guild:
            await log.send(f"```diff\n{datetime.now()} | {before.author} edited their message in #{before.channel}:\n-{before.content}\n+{after.content}\n```")
        else:
            return False

    # When a message is deleted
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        guild = self.client.get_guild(guild_id)
        log = self.client.get_channel(log_id)

        if message.author == self.client.user:
            return False
        if message.guild == guild:
            await log.send(f"```diff\n{datetime.now()} | {message.author} deleted their message in #{message.channel}:\n-{message.content}\n```")
        else: return False


def setup(client):
    client.add_cog(Forum_Events(client))
