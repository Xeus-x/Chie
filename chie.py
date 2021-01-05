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
from core import reactor as core
from utils import config
from utils import event_logger

# Variables
token = config.get_token
prefix = config.get_prefix
intents = discord.Intents().all()
shards = config.shards

if config.sharding == True:
    commands.AutoShardedBot(prefix, shard_count = shards, intents = intents)
    event_logger.INFO(__name__, "Generated %d shards" % shards)

elif config.sharding == False:
    commands.Bot(prefix, intents = intents)

client = commands.Bot(prefix, intents = intents)

@client.event
async def on_ready():
    await client.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = 'over you.'))
    event_logger.INFO(__name__, '{0.user} is online.'.format(client))

core.startup(client, token)
