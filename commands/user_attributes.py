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
import json
import bot
from discord.ext import commands

class UserStats(commands.Cog):
    def __init__(self, client):
        self.client = client

    # (For testing purposes only)
    """
    @commands.command()
    async def give_royalcredits(self, ctx, mention:discord.Member = None, amount = None):
        if ctx.author.id == bot.owner:
            if amount is None:
                await ctx.send("Master, you can't send nothing to anyone!")
                return

            else:
                amount = int(amount)

                if amount < 0:
                    await ctx.send("That's impossible! You can't send a negative amount!.")
                    return
                else:
                    users = await self.fetch_user_profile()
                    if str(mention.id) in users:
                        user = mention
                        users[str(user.id)]["stats"]["royal_credits"] += amount
                        with open('./data/user_data.json', 'w') as f:
                            json.dump(users, f, indent=4)
                        await ctx.send(f"**Nhalrath** gave {mention} `{amount}` Royal Credits!")
                    else:
                        await ctx.send(f"It seems that **{mention}** is not registered yet.")
        else:
            await ctx.send("You don't have the authority to use that!")
    """

    # User Profile
    @commands.command(aliases = ['pr'])
    async def profile(self, ctx, mention:discord.Member=None):
        if mention is None:
            users = await self.fetch_user_profile()
            user = ctx.author
            await self.check_user_profile(user)
            card_owner = user
        else:
            users = await self.fetch_user_profile()
            user = mention
            if str(user.id) in users:
                await self.check_user_profile(discord.Member)
                card_owner = mention
            else:
                await ctx.send(f"It seems that **{mention}** is not registered yet.")
                return False

        profile_card = discord.Embed(
            title = f"{card_owner}'s Profile Card'",
            color = discord.Color.green()
        )
        profile_card.set_thumbnail(
            url = card_owner.avatar_url
        )
        profile_card.add_field(
            name = 'Level',
            value = f'{users[str(user.id)]["stats"]["level"]}',
            inline = True
        )
        profile_card.add_field(
            name = 'Experience',
            value = f'{users[str(user.id)]["stats"]["exp"]}',
            inline = True
        )
        profile_card.add_field(
            name = 'Reputation',
            value = f'{users[str(user.id)]["stats"]["reputation"]}',
            inline = True
        )
        profile_card.add_field(
            name = 'Balance',
            value = f'{users[str(user.id)]["stats"]["credits"]}',
            inline = True
        )
        profile_card.add_field(
            name = 'Royal Credits',
            value = f'{users[str(user.id)]["stats"]["royal_credits"]}',
            inline = True
        )
        profile_card.add_field(
            name = 'Courage',
            value = f'{users[str(user.id)]["stats"]["courage"]}',
            inline = True
        )
        profile_card.add_field(
            name = 'str',
            value = f'{users[str(user.id)]["stats"]["str"]}',
            inline = True
        )
        profile_card.add_field(
            name = 'def',
            value = f'{users[str(user.id)]["stats"]["def"]}',
            inline = True
        )
        profile_card.add_field(
            name = 'mana',
            value = f'{users[str(user.id)]["stats"]["mana"]}',
            inline =True
        )
        profile_card.add_field(
            name = 'int',
            value = f'{users[str(user.id)]["stats"]["int"]}',
            inline = True
        )

        await ctx.send(embed = profile_card)

    # Inventory
    @commands.command(aliases = ['inv'])
    async def inventory(self, ctx, mention:discord.Member=None):
        if mention is None:
            users = await self.fetch_user_profile()
            user = ctx.author
            await self.check_user_profile(user)
            card_owner = user
        else:
            users = await self.fetch_user_profile()
            user = mention
            if str(user.id) in users:
                await self.check_user_profile(discord.Member)
                card_owner = mention
            else:
                await ctx.send(f"It seems that **{mention}** is not registered yet.")
                return False

        inventory_card = discord.Embed(
            title = f"{card_owner}'s Inventory",
            color = discord.Color.green()
        )
        inventory_card.set_thumbnail(
            url = card_owner.avatar_url
        )
        inventory_card.add_field(
            name = 'Items',
            value = str(users[str(user.id)]["inventory"]).replace("{", "").replace("}", "").replace("'", "**").replace(":", " ="),
            inline = False
        )

        await ctx.send(embed = inventory_card)

    # Bookshelf
    @commands.command(aliases = ['books'])
    async def bookshelf(self, ctx, mention:discord.Member=None):
        if mention is None:
            users = await self.fetch_user_profile()
            user = ctx.author
            await self.check_user_profile(user)
            card_owner = user
        else:
            users = await self.fetch_user_profile()
            user = mention
            if str(user.id) in users:
                await self.check_user_profile(discord.Member)
                card_owner = mention
            else:
                await ctx.send(f"It seems that **{mention}** is not registered yet.")
                return False

        bookshelf = discord.Embed(
            title = f"{card_owner}'s Bookshelf",
            color = discord.Color.green()
        )
        bookshelf.set_thumbnail(
            url = card_owner.avatar_url
        )
        bookshelf.add_field(
            name = 'Books',
            value = str(users[str(user.id)]["bookshelf"]).replace("{", "").replace("}", "").replace("'", "**").replace(":", " ="),
            inline = False
        )

        await ctx.send(embed = bookshelf)

    # Registers New Member
    @commands.Cog.listener()
    async def on_member_join(self, member):
        users = await self.check_user_profile(member)

        with open('./data/user_data.json', 'w') as f:
            json.dump(users, f, indent=4)

    # Message Experience
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        users = await self.check_user_profile(message.author)
        await self.exp_gain(users, message.author, 1)
        await self.lvl_up(users, message.author, message.channel)

        with open('./data/user_data.json', 'w') as f:
            json.dump(users, f, indent=4)

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

    #################################################################################
    #################################################################################

    # Reputation
    @commands.command(aliases = ['rep'])
    @commands.cooldown(1, 86400, commands.BucketType.user)
    async def reputation(self, ctx, mention:discord.Member = None):
        if mention is None:
            await ctx.send("Please specify a user.")
            await ctx.command.reset_cooldown(ctx)

        elif mention == ctx.author:
            await ctx.send("You can't give a reputation to yourself!")
            await ctx.command.reset_cooldown(ctx)

        else:
            amount = 1

            users = await self.fetch_user_profile()
            if str(mention.id) in users:
                user = mention
                users[str(user.id)]["stats"]["reputation"] += amount
                with open('./data/user_data.json', 'w') as f:
                    json.dump(users, f, indent=4)
                await ctx.send(f"**{ctx.author}** gave **{mention}** a reputation point!")
            else:
                await ctx.send(f"It seems that **{mention}** is not registered yet.")
                await ctx.command.reset_cooldown(ctx)


def setup(client):
    client.add_cog(UserStats(client))
