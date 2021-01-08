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

# This file may be stored in the utils folder, but there's actually
# no need to use this in other files aside from chie.py

import os
import yaml

def __parse(var):
    config_variables = open("config.yml", "r")
    parsed_yaml = yaml.load(config_variables, Loader = yaml.FullLoader)
    val = parsed_yaml[var]

    return val

switch = "use_system_environment"
sharding = __parse("use_sharding")
shards = __parse("shard_count")

if __parse(switch) == True:
    get_token = os.environ["TOKEN"]
    get_tgg_token = os.environ["TGGTOKEN"]
    get_prefix = os.environ["PREFIX"]
    get_owner = os.environ["OWNERID"]

elif __parse(switch) == False:
    get_token = __parse("TOKEN")
    get_tgg_token = __parse("TGGTOKEN")
    get_prefix = __parse("PREFIX")
    get_owner = __parse("OWNERID")
