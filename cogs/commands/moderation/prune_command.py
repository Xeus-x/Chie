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
from discord.ext import commands
from utils import event_logger

class Prune(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['clrmsg', 'purge'])
    @commands.has_permissions(manage_messages = True)
    async def prune(self, ctx, *, amount=1):
        if amount >= 101:
            await ctx.send("Sorry, but I can't handle that amount `max: 100`")
            event_logger.INFO(__name__, '{} tried to delete {} messages.'.format(ctx.author, amount))
            return False
        else:
            amount += 1
            await ctx.channel.purge(limit=amount)

def setup(client):
    client.add_cog(Prune(client))
