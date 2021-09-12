import os
import asyncio
from config import Config
from pyrogram import Client

bot = Client(
    "VideoPlayer",
    Config.API_ID,
    Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)
bot.start()
ok = bot.get_me()
USERNAME = ok.username
