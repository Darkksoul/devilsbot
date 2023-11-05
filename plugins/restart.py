import re, asyncio, os, sys
from pyrogram import Client, filters, enums
from pyrogram.types import *
from config import Config
from bot import Client


@Client.on_message(filters.private & filters.command(["restart", "r"]) & filters.user(Config.OWNER) ) 
async def stop_button(bot, message):
    msg = await bot.send_message(text="<i>Restarting.....</i>", chat_id=message.chat.id)       
    await asyncio.sleep(10)
    await msg.edit("<i>๏[-ิ_•ิ]๏ bot restarted !</i>")
    os.execl(sys.executable, sys.executable, *sys.argv)
