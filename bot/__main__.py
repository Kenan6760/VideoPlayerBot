import os
import sys
import asyncio
from config import Config
from bot.safone.nopm import User
from pyrogram import Client, idle

Bot = Client(
    ":memory:",
    Config.API_ID,
    Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="bot.safone"),
)
if not os.path.isdir("./downloads"):
    os.makedirs("./downloads")

Bot.start()
User.start()
print("\n[INFO] - STARTED VIDEO PLAYER BOT, JOIN @ASMSAFONE !")

idle()
Bot.stop()
User.stop()
print("\n[INFO] - STOPPED VIDEO PLAYER BOT, JOIN @ASMSAFONE !")
