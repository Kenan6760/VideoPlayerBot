"""
VideoPlayerBot, Telegram Video Chat Bot
Copyright (c) 2021  Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
import re
from dotenv import load_dotenv

load_dotenv()

class db:
    VIDEO_CALL = {}
    AUDIO_CALL = {}

class Config:
    ADMIN = os.environ.get("AUTH_USERS", "1620352911")
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    API_ID = int(os.environ.get("API_ID", "6"))
    CHAT_ID = list(set(int(x) for x in os.environ.get("CHAT_ID", "-1001256814964").split()))
    API_HASH = os.environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1990237992:AAFReOKtMElh4fNkIm-KWHsely7kvSRU9og")
    REPLY_MESSAGE = os.environ.get("REPLY_MESSAGE", "1620352911")
    if REPLY_MESSAGE:
        REPLY_MESSAGE = REPLY_MESSAGE
    else:
        REPLY_MESSAGE = None
    SESSION_STRING = os.environ.get("SESSION_STRING", "1ApWapzMBu6MeNspIn0Hj7b58kD34iyfT0S-ESB-NTuvA7vYGDHFGW6uSKspnDWxluYte3htx30cmBelueOGslej-sgjYHkt5CMfoVdduQHsN6Lxz2l6g2Xi0cL0V_w5Mo72SZDY-cPw7ch7HQMijjjFNQOkYTqkPExG9zkxkuZ9BBJlBQyp3Bd0Th3GewE6b5tKn1B_0EQmjFd5u7rjifhIWR5_XccQY5Co35weT6-WIK5PYttVn7rPk3f0YNZNwU-oosPoxQkU3V_QB8bsl3uDVhKfQPMvntdQt0LZ52TXN77lMjaTe5vt2ypOh0VZK8IwnvwxTutiOymGQ8jHLIu1GJ7Mkv2k=")
