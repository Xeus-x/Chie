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

path_commands = "cogs.commands."
path_listeners = "cogs.event_listeners."

cogs_commands = [
    path_commands + "miscellaneous.choose_command",
    path_commands + "miscellaneous.dice_command",
    path_commands + "miscellaneous.ping_command",
    path_commands + "miscellaneous.say_command",
    path_commands + "moderation.prune_command"
        ]

cogs_listeners = [
    path_listeners + "topGG"
        ]

cogs_debug = []


def startup(client, token):
    client.remove_command("help")

    for listener in cogs_listeners:
        client.load_extension(listener)

    for command in cogs_commands:
        client.load_extension(command)

    client.run(token)
