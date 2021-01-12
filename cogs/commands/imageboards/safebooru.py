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
import random
import requests
from utils import json_parser
from discord.ext import commands

imageboard = "https://safebooru.donmai.us"

class SafebooruCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def safebooru(self, ctx, *, tag = None):
        if tag == None:
            request = requests.get("%s/posts/random.json" % (imageboard))
            result = request.json()['file_url']
            
            await ctx.send(result)

        else:
            search = requests.get("%s/tags.json?search[name_matches]=%s*" % (imageboard, tag[0]))
            result = search.json()
            filtered_result = result[random.randrange(len(result))]['id']
            link = requests.get("%s/posts/%s.json" % (imageboard, filtered_result))
            image = link.json()['file_url']

            await ctx.send(image)

def setup(client):
    client.add_cog(SafebooruCommand(client))
