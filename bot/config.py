#    This file is part of the FileSharing distribution.
#    Copyright (c) 2022 kaif-00z
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in
# <https://github.com/kaif-00z/FileSharingBot/blob/main/License> .


from decouple import config


class Var:
    STORAGE_CHANNEL = config("-1001903781867", cast=int)
    API_HASH = config("23b6e6cf6384f716776366282e229dba")
    APP_ID = config("7190769", cast=int)
    BOT_TOKEN = config("6178177351:AAFm4LyxR5ziL6YLd0VE0Dqq8T2EBeeaheU")
    REDIS_URI = config("redis-13928.c84.us-east-1-2.ec2.cloud.redislabs.com:13928", default=None)
    REDIS_PASS = config("QWEasd123$", default=None)
    OWNER_ID = config("5729559392", cast=int)
