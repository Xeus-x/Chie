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

path_listeners = "cogs.event_listeners."

cogs_commands = ["miscellaneous.avatar_command",
                 "miscellaneous.choose_command",
                 "miscellaneous.dice_command",
                 "miscellaneous.ping_command",
                 "miscellaneous.say_command",
                 "informations.help_command",
                 "informations.userinfo_command",
                 "informations.guildinfo_command",
                 "imageboards.safebooru",
                 "imageboards.danbooru",
                 "imageboards.actions.hug_command",
                 "imageboards.actions.slap_command",
                 "imageboards.actions.kiss_command",
                 "moderation.prune_command"]

def startup(client, token):
    client.remove_command("help")

    for listener in ["cogs.event_listeners." + path for path in ["topGG", "error_listener"]]:
        client.load_extension(listener)

    for command in ["cogs.commands." + path for path in cogs_commands]:
        client.load_extension(command)

    client.run(token)
