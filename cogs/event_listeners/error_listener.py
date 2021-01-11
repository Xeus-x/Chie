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

class ErrorListener(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            return
            
        elif isinstance(error, commands.CommandOnCooldown):
            def convert(seconds):
                minute, second = divmod(seconds, 60)
                hour, minute = divmod(min, 60)
                return "**%dh**, **%02dm**, **%02ds**" % (hour, minute, second)
            await ctx.send("Not too fast! You can use this command again in {}".format(convert(error.retry_after)))

def setup(client):
    client.add_cog(ErrorListener(client))
