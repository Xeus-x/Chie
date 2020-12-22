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
import asyncio
import list
import json
import random
from discord.ext import commands

class UserGrowth(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Experience Gain
    async def exp_gain(self, users, user, exp_amt):
        users[str(user.id)]["stats"]["exp"] += exp_amt

    # Level Up
    async def lvl_up(self, users, user, channel):
        experience = users[str(user.id)]["stats"]["exp"]
        lvl_initial = users[str(user.id)]["stats"]["level"]
        lvl_end = int(experience ** (1/10))

        if lvl_initial < lvl_end:
            await channel.send(f"**{user}** advanced to level {lvl_end}!")
            users[str(user.id)]["stats"]["level"] = lvl_end


    # Check User Profile
    async def check_user_profile(self, user):
        users = await self.fetch_user_profile()

        if str(user.id) in users:
            return users
        else:
            users[str(user.id)] = {}
            users[str(user.id)]["stats"] = {}
            users[str(user.id)]["inventory"] = {}
            users[str(user.id)]["bookshelf"] = {}
            users[str(user.id)]["stats"]["level"] = 0
            users[str(user.id)]["stats"]["exp"] = 0
            users[str(user.id)]["stats"]["str"] = 0
            users[str(user.id)]["stats"]["def"] = 0
            users[str(user.id)]["stats"]["mana"] = 0
            users[str(user.id)]["stats"]["int"] = 0
            users[str(user.id)]["stats"]["courage"] = 0
            users[str(user.id)]["stats"]["reputation"] = 0
            users[str(user.id)]["stats"]["credits"] = 0
            users[str(user.id)]["stats"]["royal_credits"] = 0
            users[str(user.id)]["inventory"]["Dagger"] = 1
            users[str(user.id)]["bookshelf"]["Tattered Book"] = 1
        with open('./data/user_data.json', 'w') as f:
            json.dump(users, f, indent=4)
        return users

    # User Profile
    async def fetch_user_profile(self):
        with open('./data/user_data.json', 'r') as f:
            users = json.load(f)
        return users

    # Commissions
    async def fetch_commissions(self):
        with open('./data/commissions.json', 'r') as f:
            commissions = json.load(f)
        return commissions

    ###########################################################################
    ###########################################################################

    # Train
    @commands.command()
    @commands.cooldown(1, 10800, commands.BucketType.user)
    async def train(self, ctx):
        await self.check_user_profile(ctx.author)
        user = ctx.author
        users = await self.fetch_user_profile()
        gain = random.randrange(5, 20)

        if gain == 20:
            users[str(user.id)]["stats"]["exp"] += gain
            users[str(user.id)]["stats"]["str"] += 1
            with open('./data/user_data.json', 'w') as f:
                json.dump(users, f, indent=4)
            await ctx.send("That was a great session! You almost fainted, but became slightly stronger!")
            await ctx.send(f"You gained `{gain}` exp and `1` str!")

        elif gain == range(1, 5):
            users[str(user.id)]["stats"]["exp"] += gain
            with open('./data/user_data.json', 'w') as f:
                json.dump(users, f, indent=4)
            await ctx.send("You got tired easily, and didn't made much progress...")
            await ctx.send(f"You gained `{gain}` exp!")

        else:
            users[str(user.id)]["stats"]["exp"] += gain
            with open('./data/user_data.json', 'w') as f:
                json.dump(users, f, indent=4)
            await ctx.send(f"{random.choice(list.train_responses)}")
            await ctx.send(f"You gained `{gain}` exp!")

    # Commission
    @commands.command()
    @commands.cooldown(1, 86400, commands.BucketType.user)
    async def commission(self, ctx, type = None):
        await self.check_user_profile(ctx.author)
        user = ctx.author
        users = await self.fetch_user_profile()
        commissions = await self.fetch_commissions()

        if type is None:
            await ctx.send("Please specify what type of commission you would like to take.")
            ctx.command.reset_cooldown(ctx)
            return False

        elif type == 'exp':
            choices = eval(commissions["exp_1"]["description"])
            rewards = int(eval(commissions["exp_1"]["rewards"]))
            description = random.choice(choices)

            cmmsn = discord.Embed(
                title = "Commission",
                color = discord.Color.blue()
            )
            cmmsn.set_footer(
                icon_url = ctx.author.avatar_url,
                text = ctx.author,
            )
            cmmsn.add_field(
                name = 'Description',
                value = description,
                inline = False
            )
            cmmsn.add_field(
                name = 'Rewards',
                value = '3-8 exp',
                inline = True
            )
            cmmsn.add_field(
                name = 'Type',
                value = type,
                inline = True
            )
            cmmsn.add_field(
                name = 'Difficulty',
                value = '1',
                inline = True
            )

            msg = await ctx.send(embed = cmmsn)

            await msg.add_reaction('\u2705')
            await msg.add_reaction('\u274e')

            def check(reaction, user):
                return user.id == ctx.author.id and reaction.message.channel.id == ctx.channel.id and \
                        str(reaction.emoji) in ['\u2705', '\u274e']

            while True:
                try:
                    reaction, user = await self.client.wait_for('reaction_add', check = check, timeout = 30)
                except asyncio.TimeoutError:
                    await msg.clear_reactions()
                    ctx.command.reset_cooldown(ctx)
                    break

                else:
                    if str(reaction.emoji) == '\u2705':
                        await msg.clear_reactions()
                        await ctx.send(f"**{ctx.author}** accepted their commission\n")

                        users[str(user.id)]["stats"]["exp"] += rewards
                        with open('./data/user_data.json', 'w') as f:
                            json.dump(users, f, indent=4)
                        await ctx.send(f"**{ctx.author}** received `{rewards}` exp!")

                    if str(reaction.emoji) == '\u274e':
                        await msg.clear_reactions()
                        await ctx.send(f"**{ctx.author}** declined their commission.")
                        ctx.command.reset_cooldown(ctx)
                        break

        elif type == 'credits':
            choices = eval(commissions["credits_1"]["description"])
            rewards = eval(commissions["credits_1"]["rewards"])
            description = random.choice(choices)

            cmmsn = discord.Embed(
                title = "Commission",
                color = discord.Color.blue()
            )
            cmmsn.set_footer(
                icon_url = ctx.author.avatar_url,
                text = ctx.author,
            )
            cmmsn.add_field(
                name = 'Description',
                value = description,
                inline = False
            )
            cmmsn.add_field(
                name = 'Rewards',
                value = '20-50 credits',
                inline = True
            )
            cmmsn.add_field(
                name = 'Type',
                value = type,
                inline = True
            )
            cmmsn.add_field(
                name = 'Difficulty',
                value = '1',
                inline = True
            )

            msg = await ctx.send(embed = cmmsn)

            await msg.add_reaction('\u2705')
            await msg.add_reaction('\u274e')

            def check(reaction, user):
                return user.id == ctx.author.id and reaction.message.channel.id == ctx.channel.id and \
                        str(reaction.emoji) in ['\u2705', '\u274e']

            while True:
                try:
                    reaction, user = await self.client.wait_for('reaction_add', check = check, timeout = 30)
                except asyncio.TimeoutError:
                    await msg.clear_reactions()
                    ctx.command.reset_cooldown(ctx)
                    break

                else:
                    if str(reaction.emoji) == '\u2705':
                        await msg.clear_reactions()
                        await ctx.send(f"**{ctx.author}** accepted their commission\n")

                        users[str(user.id)]["stats"]["credits"] += rewards
                        with open('./data/user_data.json', 'w') as f:
                            json.dump(users, f, indent=4)
                        await ctx.send(f"**{ctx.author}** received `{rewards}` credits!")

                    if str(reaction.emoji) == '\u274e':
                        await msg.clear_reactions()
                        await ctx.send(f"**{ctx.author}** declined their commission.")
                        ctx.command.reset_cooldown(ctx)
                        break

        else:
            await ctx.send(f"It seems that there are no commisions for `{type}`.")
            ctx.command.reset_cooldown(ctx)
            return False


def setup(client):
    client.add_cog(UserGrowth(client))
