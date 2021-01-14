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
#45 Lines
import logging

def debugInit(logger, level, loggerType, msg):
    logger = logging.getLogger(logger)
    logger.setLevel(level)
    handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='a')
    handler.setFormatter(logging.Formatter('%(asctime)s | %(levelname)s | %(name)s | %(message)s'))
    logger.addHandler(handler) 
    if loggerType == 1:
        logger.info(msg)
    elif loggerType == 2:
        logger.debug(msg)
    elif loggerType == 3:
        logger.warning(msg)
    else:
        print("Logger: unsupported type")
    print(msg)

def INFO(logger, msg):
    level = logging.INFO
    loggerType = 1
    logger = debugInit(logger, level, loggerType, msg)

def DEBUG(logger, msg):
    level = logging.DEBUG
    loggerType = 2
    logger = debugInit(logger, level, loggerType, msg)

def WARNING(logger, msg):
    level = logging.WARNING
    loggerType = 3
    logger = debugInit(logger, level, loggerType, msg)
