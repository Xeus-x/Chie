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
import list
import embed_list
from discord.ext import commands

class Miscellaneous(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Commands
    @commands.command() # A template for sending messages.
    async def template(self, ctx):
        await ctx.send('template')

    @commands.command()
    async def say(self, ctx, *, arg):
        await ctx.send(arg)

    @commands.command(aliases = ['8ball'])
    async def _8ball(self, ctx, *, question):
        await ctx.send(random.choices(list._8ball_responses, weights=[20, 20, 20, 20, 20, 1, 20, 20, 20], k=1)[0])

    @commands.command()
    async def throw(self, ctx, mention:discord.Member):
        await ctx.send(f"Threw {random.choice(list.throw_responses)} at **{mention}**!")

    @commands.command(aliases = ['roll'])
    async def dice(self, ctx, face = 6):
        await ctx.send(f':game_die:{random.randrange(1, int(face))} (1-{face})')

    @commands.command()
    async def choose(self, ctx, *, choice):
        bot_choice = choice.replace(" ","").split(",")
        await ctx.send(f"I choose `{random.choice(bot_choice)}`.")
"""
class Fun_Commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Fun Commands

    # Beg
    @commands.command()
    async def beg(self, ctx, mention:discord.Member = None):
        if mention is None:
            file = discord.File(random.choice(embed_list.gif_beg), filename="beg.gif")
            embed = discord.Embed(color = discord.Color.blue())
            embed.set_image(url="attachment://beg.gif")
            await ctx.send(f"> {ctx.author} is begging money at me.")
            await ctx.send(file=file, embed=embed)
        else:
            file = discord.File(random.choice(embed_list.gif_beg), filename="beg.gif")
            embed = discord.Embed(color = discord.Color.blue())
            embed.set_image(url="attachment://beg.gif")
            await ctx.send(f"> **{ctx.author}** is begging **{mention}** for money.")
            await ctx.send(file=file, embed=embed)

    # Laugh
    @commands.command()
    async def laugh(self, ctx, mention:discord.Member = None):
        if mention is None:
            file = discord.File(random.choice(embed_list.gif_laugh), filename="laugh.gif")
            embed = discord.Embed(color = discord.Color.blue())
            embed.set_image(url="attachment://laugh.gif")
            await ctx.send("> *Laughs at you.")
            await ctx.send(file=file, embed=embed)
        else:
            file = discord.File(random.choice(embed_list.gif_laugh), filename="laugh.gif")
            embed = discord.Embed(color = discord.Color.blue())
            embed.set_image(url="attachment://laugh.gif")
            await ctx.send(f"> **{ctx.author}** laughs at **{mention}**.")
            await ctx.send(file=file, embed=embed)

    # Pat
    @commands.command()
    async def pat(self, ctx, mention:discord.Member = None):
        if mention is None:
            file = discord.File(random.choice(embed_list.gif_pat), filename="pat.gif")
            embed = discord.Embed(color = discord.Color.blue())
            embed.set_image(url="attachment://pat.gif")
            await ctx.send("> *Pats you.")
            await ctx.send(file=file, embed=embed)
        else:
            file = discord.File(random.choice(embed_list.gif_pat), filename="pat.gif")
            embed = discord.Embed(color = discord.Color.blue())
            embed.set_image(url="attachment://pat.gif")
            await ctx.send(f"> **{ctx.author}** pats **{mention}**.")
            await ctx.send(file=file, embed=embed)

    # Slap
    @commands.command()
    async def slap(self, ctx, mention:discord.Member = None):
        if mention is None:
            file = discord.File(random.choice(embed_list.gif_slap), filename="slap.gif")
            embed = discord.Embed(color = discord.Color.blue())
            embed.set_image(url="attachment://slap.gif")
            await ctx.send("> *Slaps you.")
            await ctx.send(file=file, embed=embed)
        else:
            file = discord.File(random.choice(embed_list.gif_slap), filename="slap.gif")
            embed = discord.Embed(color = discord.Color.blue())
            embed.set_image(url="attachment://slap.gif")
            await ctx.send(f"> **{ctx.author}** slaps **{mention}**.")
            await ctx.send(file=file, embed=embed)

    # Smile
    @commands.command()
    async def smile(self, ctx, mention:discord.Member = None):
        if mention is None:
            file = discord.File(random.choice(embed_list.gif_smile), filename="smile.gif")
            embed = discord.Embed(color = discord.Color.blue())
            embed.set_image(url="attachment://smile.gif")
            await ctx.send("> *smiles at you.")
            await ctx.send(file=file, embed=embed)
        else:
            file = discord.File(random.choice(embed_list.gif_smile), filename="smile.gif")
            embed = discord.Embed(color = discord.Color.blue())
            embed.set_image(url="attachment://smile.gif")
            await ctx.send(f"> **{ctx.author}** smiles at **{mention}**.")
            await ctx.send(file=file, embed=embed)
"""

def setup(client):
    client.add_cog(Moderation(client))
    client.add_cog(Miscellaneous(client))
