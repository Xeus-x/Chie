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
import os
import json
import time
from discord.ext import commands

# It is not recommended to use all intents
intents = discord.Intents().all()

# Change these values to String if you are trying to self-host your bot
token = os.environ['TOKEN']
tggToken = os.environ['TGGTOKEN']
passw = os.environ['PASSWORD']
owner = os.environ['OWNER']

# Checks the current server's prefix.
def get_prefix(client, message):
    with open('./data/prefixes.json', 'r') as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix = get_prefix, intents = intents)

# Remove built-in help command
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = 'over you.'))
    print('{0.user} is online.'.format(client))

# Assigns a new guild with a default prefix. (You might want to comment this out, I forgot to fix this one)
@client.event
async def on_guild_join(guild):
    with open('./data/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '>'

    with open('./data/prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

# Sets the guild's custom prefix.
@client.command()
@commands.has_permissions(administrator = True)
async def setprefix(ctx, prefix):
    with open('./data/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('./data/prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    await ctx.send(f"Prefix changed to `{prefix}`.")

#Bot Status
@client.command()
async def ping(ctx):
    websocket = round(client.latency * 1000)
    timeStart = time.perf_counter()
    msg = await ctx.send("Pinging...")

    timeEnd = time.perf_counter()
    await msg.edit(content = f"**Ping:** {round((timeEnd - timeStart) * 1000)}ms | **Websocket:** {websocket}ms")


@client.command()
async def status(ctx):
    await ctx.send("```yaml\n[Version]: VERSION\n[Library]: LIBRARY\n```")

# Load and Unload (For manintenance only.)
# Comment this if your are not testing your bot
@client.command()
async def load(ctx, extension, ext):
    if ctx.author.id == owner:
        client.load_extension(f'{ext}.{extension}')
    else:
        return False

@client.command()
async def unload(ctx, extension, ext):
    if ctx.author.id == owner:
        client.unload_extension(f'{ext}.{extension}')
    else:
        return False

@client.command()
async def reboot(ctx, extension, ext):
    if ctx.author.id == owner:
        client.unload_extension(f'{ext}.{extension}')
        client.load_extension(f'{ext}.{extension}')
    else:
        return False

# Loop Load
# Shouldn't have used for loop.
for files in os.listdir('./commands'):
    if files.endswith('.py'):
        client.load_extension(f'commands.{files[:-3]}')

for files in os.listdir('./events'):
    if files.endswith('.py'):
        client.load_extension(f'events.{files[:-3]}')

client.run(token)
