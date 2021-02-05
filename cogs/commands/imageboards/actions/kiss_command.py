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

class KissCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    def embedBuilder(self, title):
        image = requests.get("https://api.kurosama.tk/v1/kiss")
        url = image.json()[0]

        embed = discord.Embed(
            title = title,
            color = 0xFFC0CB
        )
        embed.set_image(
            url = url
        )
        embed.set_footer(
            text = ctx.author,
            icon_url = ctx.author.avatar_url
        )

        return embed
    
    @commands.command()
    async def kiss(self, ctx, mention:discord.Member=None):
        if mention == None:
            await ctx.send(embed = self.embedBuilder("\**Kissed you\**"))
        else:
            await ctx.send(embed = self.embedBuilder("%s kissed %s..." % (ctx.author.display_name, mention.display_name)))

def setup(client):
    client.add_cog(KissCommand(client))
