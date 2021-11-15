import os
import logging
import asyncio
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup





@Client.on_message(filters.command("start"))
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""✨ **Welcome {message.from_user.mention()} !**\n
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Add me to your Group ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                                                                       
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )
