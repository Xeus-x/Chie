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

import yaml

def __parse(pri, sub):
    config_variables = open("bot_info.yml", "r")
    parsed_yaml = yaml.load(config_variables, Loader = yaml.FullLoader)
    val = parsed_yaml[pri][sub]

    return val

name = __parse("bot", "name")
github = __parse("bot", "github")

version_MAJOR = __parse("version", "MAJOR")
version_MINOR = __parse("version", "MINOR")
version_REVISION = __parse("version", "REVISION")

version_STRING = "v%d.%d.%d" % (version_MAJOR, version_MINOR, version_REVISION)
