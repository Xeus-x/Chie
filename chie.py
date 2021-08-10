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

import os
import discord
import json

from datetime import datetime
from discord.ext import commands
from chieUtils import logger

# Config
try:
    with open("config.json", 'r') as f:
        config = json.load(f)

        USE_SYS_ENV = True if config["USE_SYS_ENV"] else False

        USE_SHARDING    = os.environ["USE_SHARDING"]    if USE_SYS_ENV else config["USE_SHARDING"]
        TOKEN           = os.environ["TOKEN"]           if USE_SYS_ENV else config["TOKEN"]
        TGG_TOKEN       = os.environ["TGG_TOKEN"]       if USE_SYS_ENV else config["TGG_TOKEN"]
        COMMAND_PREFIX  = os.environ["COMMAND_PREFIX"]  if USE_SYS_ENV else config["COMMAND_PREFIX"]
        OWNER_ID        = os.environ["OWNER_ID"]        if USE_SYS_ENV else config["OWNER_ID"]
        SHARD_COUNT     = os.environ["SHARD_COUNT"]     if USE_SYS_ENV else config["SHARD_COUNT"]
except KeyError:
    print("Failed to initialize config constants")

if USE_SHARDING:
    client = commands.AutoShardedBot(COMMAND_PREFIX, shard_count = SHARD_COUNT, intents = discord.Intents().all())
    logger.INFO(__name__, f"Generated {SHARD_COUNT} shards")

else:
    client = commands.Bot(COMMAND_PREFIX, intents = discord.Intents().all())

client.remove_command("help")

# Load cogs and commands
listeners_path = "cogs.event_listeners."

commands_path = ["miscellaneous.avatar_command",
                 "miscellaneous.choose_command",
                 "miscellaneous.dice_command",
                 "miscellaneous.ping_command",
                 "miscellaneous.say_command",

                 "moderation.unban_command",
                 "moderation.prune_command",

                 "informations.invite_command",
                 "informations.userinfo_command",
                 "informations.guildinfo_command",
                 "informations.help_command",
                 "informations.support_command",

                 "imageboards.actions.hug_command",
                 "imageboards.actions.slap_command",
                 "imageboards.actions.kiss_command",

                 "imageboards.danbooru",
                 "imageboards.safebooru"]

@client.event
async def on_ready():
    print(f"Live {datetime.now().strftime('%m-%d-%Y')}")
    await client.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = 'over you.'))
    logger.INFO(__name__, '{0.user} is online.'.format(client))

for listener in ["cogs.event_listeners." + path for path in ["topGG", "error_listener"]]:
    client.load_extension(listener)

for command in ["cogs.commands." + path for path in commands_path]:
    client.load_extension(command)

client.run(TOKEN)