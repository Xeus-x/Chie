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
import random
from discord.ext import commands

class Economy(commands.Cog):
    def __init__(self, client):
        self.client = client

    # balance
    @commands.command(aliases=['bal'])
    async def balance(self, ctx, mention:discord.Member=None):
        if mention is None:
            users = await self.check_user_profile(ctx.author)
            user = ctx.author
            bal_amt = users[str(user.id)]["stats"]["credits"]
        else:
            users = await self.fetch_user_profile()
            user = mention
            if str(user.id) in users:
                users = await self.check_user_profile(discord.Member)
                bal_amt = users[str(user.id)]["stats"]["credits"]
            else:
                bal_amt = f"It seems that **{mention}** is not registered yet."
        await ctx.send(bal_amt)

    # Transfer Money
    @commands.command(aliases = ['give'])
    async def transfer(self, ctx, mention:discord.Member, amount=None):
        if amount is None:
            await ctx.send("Please enter the amount you are trying to send.")
            return

        bal = await self.update_balance(ctx.author)
        amount = int(amount)

        if amount > bal[0]:
            await ctx.send("You don't have enough money.")
            return
        elif amount < 0:
            await ctx.send("Please enter a valid amount.")
            return
        else:
            users = await self.fetch_user_profile()
            if str(mention.id) in users:
                await self.check_user_profile(ctx.author)
                await self.check_user_profile(discord.Member)
                await self.update_balance(ctx.author, -amount)
                await self.update_balance(mention, amount)
                await ctx.send(f"**{ctx.author}** gave **{mention}** `{amount}` credits!")
            else:
                await ctx.send(f"It seems that **{mention}** is not registered yet.")

    # Miracle (for testing purposes only)
    """
    @commands.command()
    async def miracle(self, ctx):
        await self.check_user_profile(ctx.author)
        user = ctx.author
        users = await self.fetch_user_profile()
        gain = random.randrange(100)

        users[str(user.id)]["stats"]["credits"] += gain
        with open('./data/user_data.json', 'w') as f:
            json.dump(users, f, indent=4)
        await ctx.send(f"You gained {gain} credits!")
    """

    # Balance Checker
    async def check_user_profile(self, user):
        users = await self.fetch_user_profile()

        if str(user.id) in users:
            return users
        else:
            users[str(user.id)] = {}
            users[str(user.id)]["stats"] = {}
            users[str(user.id)]["inventory"] = {}
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
        with open('./data/user_data.json', 'w') as f:
            json.dump(users, f, indent=4)
        return users

    # Update Balance
    async def update_balance(self, user, modify=0):
        users = await self.fetch_user_profile()
        users[str(user.id)]["stats"]["credits"] += modify
        with open('./data/user_data.json', 'w') as f:
            json.dump(users, f, indent=4)
        bal = [users[str(user.id)]["stats"]["credits"]]
        return bal

    # User Balance
    async def fetch_user_profile(self):
        with open('./data/user_data.json', 'r') as f:
            users = json.load(f)
        return users

    ###########################################################################
    ###########################################################################

    # Daily
    @commands.command()
    @commands.cooldown(1, 86400, commands.BucketType.user)
    async def daily(self, ctx):
        await self.check_user_profile(ctx.author)
        user = ctx.author
        users = await self.fetch_user_profile()
        multiplier = users[str(user.id)]["stats"]["level"]
        gain = random.randrange(10, 50)*multiplier

        users[str(user.id)]["stats"]["credits"] += gain
        with open('./data/user_data.json', 'w') as f:
            json.dump(users, f, indent=4)
        await ctx.send(f"You obtained your daily with an amount of `{gain}` credits!")

    @commands.command()
    @commands.cooldown(2, 21600, commands.BucketType.user)
    async def work(self, ctx):
        await self.check_user_profile(ctx.author)
        user = ctx.author
        users = await self.fetch_user_profile()
        multiplier = users[str(user.id)]["stats"]["level"]
        gain = random.randrange(5, 10)*multiplier

        users[str(user.id)]["stats"]["credits"] += gain
        with open('./data/user_data.json', 'w') as f:
            json.dump(users, f, indent=4)
        await ctx.send(f"You worked so hard, and you got paid `{gain}` credits.")

def setup(client):
    client.add_cog(Economy(client))
