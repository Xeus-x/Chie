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
import json
from discord.ext import commands

class Story(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Check Book
    async def check_book(self, book):
        books = await self.fetch_book()

        if str(book) in books:
            return books
        else:
            return False

    # Shelves
    async def fetch_book(self):
        with open('./data/shelves.json', 'r') as f:
            books = json.load(f)
        return books

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

    ###########################################################################
    ###########################################################################


    @commands.command()
    @commands.cooldown(2, 3600, commands.BucketType.user)
    async def read(self, ctx, book = None):
        if book is None:
            await ctx.send("Please pick a book.")
            ctx.command.reset_cooldown(ctx)
            return False
        else:
            books = await self.fetch_book()
            book = book
            if str(book) in books:
                users = await self.fetch_user_profile()
                user = ctx.author
                int = random.randrange(1, 50)

                await self.check_book(book)
                reading = books[str(book)]["page1"]

                with open(reading, 'r') as r:
                    rr = r.read()

                rr_embed = discord.Embed(
                    title = 'Reading a Book...',
                    color = discord.Color.red()
                )
                rr_embed.set_footer(
                    icon_url = ctx.author.avatar_url,
                    text = ctx.author
                )
                rr_embed.add_field(
                    name = 'Intro',
                    value = rr,
                    inline = False
                )

                if int == 25:
                    users[str(user.id)]["bookshelf"][str(book)] = 1
                    users[str(user.id)]["stats"]["int"] += 1
                    with open('./data/user_data.json', 'w') as f:
                        json.dump(users, f, indent=4)
                    await ctx.send(embed = rr_embed)
                else:
                    users[str(user.id)]["bookshelf"][str(book)] = 1
                    with open('./data/user_data.json', 'w') as f:
                        json.dump(users, f, indent=4)
                    await ctx.send(embed = rr_embed)
            else:
                await ctx.send(f"It seems that the book titled as {book} doesn't exists.")
                ctx.command.reset_cooldown(ctx)
                return False


def setup(client):
    client.add_cog(Story(client))
