import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
from helper.database import db
from config import Config

@Client.on_message(filters.private & filters.command("start1"))
async def start(client, message):
    user = message.from_user
    await db.add_user(client, message)
    button = InlineKeyboardMarkup([[
                InlineKeyboardButton("ᴄᴏɴᴛᴀᴄᴛ", callback_data = "apk"),
                InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data = "close")
    ]]) 
    if Config.START_PIC:
        await message.reply_photo(Config.START_PIC, caption=Txt.START_TXT.format(user.mention), reply_markup=button)       
    else:
        await message.reply_text(text=Txt.START_TXT.format(user.mention), reply_markup=button, disable_web_page_preview=True)

