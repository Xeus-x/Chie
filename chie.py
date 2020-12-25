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

from discord.ext import commands
from utils import config
from utils import event_logger

# Variables
intents = discord.Intents().all()
prefix = config.get_prefix

client = commands.Bot(prefix, intents = intents)
path_commands = "cogs.commands."
token = config.get_token

# Removes built-in command
client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = 'over you.'))
    event_logger.INFO(__name__, '{0.user} is online.'.format(client))


# Loads Command Cogs
client.load_extension(path_commands + "miscellaneous.choose_command")
client.load_extension(path_commands + "miscellaneous.ping_command")
client.load_extension(path_commands + "miscellaneous.say_command")

client.load_extension(path_commands + "moderation.prune_command")

# Startup
client.run(token)
