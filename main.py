import importlib
import re
import os
import asyncio
import logging
from pytgcalls import idle
from pyrogram import idle as pidle
from driver.veez import call_py, bot
from typing import Optional, List


if os.path.exists('log.txt'):
    with open('log.txt', 'r+') as f:
        f.truncate(0)

logging.basicConfig(
    format='%(asctime)s | %(levelname)s | %(name)s | %(message)s',
    datefmt="[%X]",
    handlers=[
        logging.FileHandler('log.txt'),
        logging.StreamHandler()],
    level=logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

LOGGER = logging.getLogger(__name__)

PM_START_TEXT = """

ʜᴏʟᴀ {}, ᴍʏ ɴᴀᴍᴇ ɪꜱ {}! ɪ ᴀᴍ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ [ᴛʜᴇ ʟᴇɢᴇɴᴅ](tg://user?id={}) ᴀɴᴅ ɪ ᴀᴍ ᴀ ꜱᴜᴘᴇʀ ᴀᴅᴍɪɴ ʙᴏᴛ.

ɪ ᴀᴍ ᴍᴀᴅᴇᴅ ɪɴ python3 ᴜꜱɪɴɢ ᴛʜɪꜱ ʟɪʙʀᴀʀʏ 𝖕𝖞𝖙𝖍𝖔𝖓-𝖙𝖊𝖑𝖊𝖌𝖗𝖆𝖒-𝖇𝖔𝖙 . ɪ ᴀᴍ ᴛᴏᴛᴀʟʟʏ ᴏᴘᴇɴ ꜱᴏᴜʀᴄᴇ. ᴍʏ ᴄᴏᴅᴇ ɪꜱ ɪɴ ᴛʜɪꜱ ᴡᴇʙ [ʟɪɴᴋ](https://github.com/lintobinoy007/tgbot) ʏᴏᴜ ᴄᴀɴ ꜱᴇᴇ ʜᴇʀᴇ.
ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴋɴᴏᴡ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅ'ꜱ ᴄʟɪᴄᴋ ᴏʀ ᴛʏᴘᴇ /help.

ɪꜰ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ Qᴜᴇʀɪᴇꜱ ᴀʙᴏᴜᴛ ᴛʜᴇ ʙᴏᴛ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ (@a_boy_is_no_one00)
ᴏʀ ᴊᴏɪɴ ᴏᴜʀ ɢʀᴏᴜᴘ (https://t.me/everythingpeople)
"""

async def mulai_bot():
    print("[VEEZ]: STARTING BOT CLIENT")
    await bot.start()
    print("[VEEZ]: STARTING PYTGCALLS CLIENT")
    await call_py.start()
    await idle()
    await pidle()
    print("[VEEZ]: STOPPING BOT & USERBOT")
    await bot.stop()

loop = asyncio.get_event_loop()
loop.run_until_complete(mulai_bot())


LOGGER.info("✅ bot has been started")
