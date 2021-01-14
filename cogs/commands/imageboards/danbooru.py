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
from utils import event_logger as logger
from utils import json_parser
from discord.ext import commands

imageboard = "https://danbooru.donmai.us"
status = requests.get(imageboard).status_code

class DanbooruCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def danbooru(self, ctx, *, tag = None):
        def embedBuilder(image, tag):
            embed = discord.Embed(
                title = "Danbooru",
                color = 0xFFC0CB,
            )
            embed.add_field(
                name = "Tags",
                value = tag,
                inline = False
            )
            embed.set_image(
                url = image
            )
            embed.set_footer(
                text = ctx.author,
                icon_url = ctx.author.avatar_url
            )

            return embed

        if status == 200:
            if ctx.channel.is_nsfw():
                if tag == None:
                    request = requests.get("%s/posts/random.json" % (imageboard))
                    image = request.json()['file_url']
                    tags = request.json()['tag_string']
                    embed = embedBuilder(image, tags)

                    await ctx.send(embed = embed)
                else:
                    search = requests.get("%s/tags.json?search[name_matches]=%s*" % (imageboard, tag[0]))
                    result = search.json()
                    filtered_result = result[random.randrange(len(result))]['id']
                    link = requests.get("%s/posts/%s.json" % (imageboard, filtered_result))
                    image = link.json()['file_url']
                    tags = link.json()['tag_string']
                    embed = embedBuilder(image, tags)

                    await ctx.send(embed = embed)
            else:
                await ctx.send("This command is only available for **NSFW channels**.")
        else:
            await ctx.send("There seems to be an error within the **Danbooru** site.")
            logger.INFO(__name__, "There's an error within the Danbooru site.")

def setup(client):
    client.add_cog(DanbooruCommand(client))
