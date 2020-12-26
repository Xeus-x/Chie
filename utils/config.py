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
import yaml

config = open("config.yml", "r")
var = yaml.load(config, Loader = yaml.FullLoader)
get_token = var["token"]
get_tgg_token = "a"# os.environ['TGGTOKEN'] or top.gg TOKEN
get_prefix = ">"# Prefix
get_owner = "a"# os.environ['OWNER'] or Owner's User ID
get_password = "a"# os.environ['PASSWORD'] or Password
