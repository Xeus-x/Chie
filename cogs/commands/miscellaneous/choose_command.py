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
import random
from discord.ext import commands

class ChooseCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["pick"])
    async def choose(self, ctx, *, choice):
        choices = choice.replace(" ","").split(",")
        await ctx.send(f"I choose **{random.choice(choices)}**!")

def setup(client):
    client.add_cog(ChooseCommand(client))
