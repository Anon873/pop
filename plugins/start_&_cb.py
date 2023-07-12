"""
Apache License 2.0
Copyright (c) 2022 @PYRO_BOTZ

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Telegram Link : https://t.me/PYRO_BOTZ 
Repo Link : https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT
License Link : https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT/blob/main/LICENSE
"""

import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
from helper.database import db
from config import Config

@Client.on_message(filters.private & filters.command("start"))
async def start(client, message):
    user = message.from_user
    await db.add_user(client, message)
    button = InlineKeyboardMarkup([[
                InlineKeyboardButton("ᴄᴏɴᴛᴀᴄᴛ", callback_data = "apk"),
                InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data = "close")
    ]]) 
    if Config.START_PIC:
        await message.reply_photo(Config.START_PIC, caption=Txt.START1_TXT.format(user.mention), reply_markup=button)       
    else:
        await message.reply_text(text=Txt.START1_TXT.format(user.mention), reply_markup=button, disable_web_page_preview=True)

@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            text=Txt.START_TXT.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup([[
                InlineKeyboardButton("ᴄᴏɴᴛᴀᴄᴛ", callback_data = "apk"),
                InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data = "close")
    ]]) 
    )


@Client.on_message((filters.private & filters.command("pvtstart")) & filters.user(Config.ADMIN))
async def start(client, message):
    user = message.from_user
    await db.add_user(client, message)                
    button = InlineKeyboardMarkup([[
        InlineKeyboardButton("•ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs•", callback_data='help')
        ],[
        InlineKeyboardButton('•ᴜᴘᴅᴀᴛᴇs•', url='https://t.me/All_Hindi_Anime'),
        InlineKeyboardButton('•sᴜᴩᴩᴏʀᴛ•', url='https://t.me/botsupportx')
        ],[
        InlineKeyboardButton('ᴀʙᴏᴜᴛ ᴜꜱ 🥀', callback_data='about')
    ]])
    if Config.START_PIC:
        await message.reply_photo(Config.START_PIC, caption=Txt.START_TXT.format(user.mention), reply_markup=button)       
    else:
        await message.reply_text(text=Txt.START_TXT.format(user.mention), reply_markup=button, disable_web_page_preview=True)
   

@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "pvtstart":
        await query.message.edit_text(
            text=Txt.START_TXT.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup([[
                InlineKeyboardButton("•ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs•", callback_data='help')
                ],[
                InlineKeyboardButton('•ᴜᴘᴅᴀᴛᴇs•', url='https://t.me/All_Hindi_Anime'),
                InlineKeyboardButton('•sᴜᴩᴩᴏʀᴛ•', url='https://t.me/botsupportx')
                ],[
                InlineKeyboardButton('ᴀʙᴏᴜᴛ ᴜꜱ 🥀', callback_data='about')
    ]])
        )
    elif data == "help":
        await query.message.edit_text(
            text=Txt.HELP_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ", callback_data="custom")
                ],[
                InlineKeyboardButton("ᴛʜᴜᴍʙɴᴀɪʟ", callback_data="thumb"),
                InlineKeyboardButton("ʀᴇɴᴀᴍᴇ ꜰɪʟᴇ", callback_data="rename")
                ],[
                InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data = "close"),
                InlineKeyboardButton("ʙᴀᴄᴋ", callback_data = "pvtstart")
    ]])
        )
    elif data == "about":
        await query.message.edit_text(
            text=Txt.ABOUT_TXT.format(client.mention),
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([[
                #⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data = "close"),
                InlineKeyboardButton("ʙᴀᴄᴋ", callback_data = "pvtstart")
            ]])            
        )
    elif data == "dev":
        await query.message.edit_text(
            text=Txt.DEV_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data = "close"),
                InlineKeyboardButton("ʙᴀᴄᴋ", callback_data = "pvtstart")
            ]])          
        )
    elif data == "apk":
        await query.message.edit_text(
            text=Txt.APK_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data = "close"),
                InlineKeyboardButton("ʙᴀᴄᴋ", callback_data = "start")
            ]])          
        )
    elif data == "rename":
        await query.message.edit_text(
            text=Txt.REX_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data = "close"),
                InlineKeyboardButton("ʙᴀᴄᴋ", callback_data = "help")
            ]])          
                                    )
    elif data == "thumb":
        await query.message.edit_text(
            text=Txt.RET_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data = "close"),
                InlineKeyboardButton("ʙᴀᴄᴋ", callback_data = "help")
            ]])          
                                     )
    elif data == "custom":
        await query.message.edit_text(
            text=Txt.REX2_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data = "close"),
                InlineKeyboardButton("ʙᴀᴄᴋ", callback_data = "help")
            ]])          
        )
    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
            await query.message.continue_propagation()
        except:
            await query.message.delete()
            await query.message.continue_propagation()


class Txt(object):
    # part of text configuration
    START_TXT = "✨ нєу ʙᴀʙʏ {} 🥀 \n\n➻ ᴛʜɪꜱ ɪꜱ ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀɴᴅ ʏᴇᴛ ᴘᴏᴡᴇʀꜰᴜʟ ʀᴇɴᴀᴍᴇ ʙᴏᴛ. \n➻ ᴜꜱɪɴɢ ᴛʜɪꜱ ʙᴏᴛ ʏᴏᴜ ᴄᴀɴ ʀᴇɴᴀᴍᴇ ᴀɴᴅ ᴄʜᴀɴɢᴇ ᴛʜᴜᴍʙɴᴀɪʟ ᴏꜰ ʏᴏᴜʀ ꜰɪʟᴇꜱ. \n➻ ʏᴏᴜ ᴄᴀɴ ᴀʟꜱᴏ ᴄᴏɴᴠᴇʀᴛ ᴠɪᴅᴇᴏ ᴛᴏ ꜰɪʟᴇ ᴀɴᴅ ꜰɪʟᴇ ᴛᴏ ᴠɪᴅᴇᴏ. \n➻ ᴛʜɪꜱ ʙᴏᴛ ᴀʟꜱᴏ ꜱᴜᴘᴘᴏʀᴛꜱ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ᴀɴᴅ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛᴀɪɴ."

    ABOUT_TXT = "➻ ᴍʏ ɴᴀᴍᴇ : {} \n➻ ᴍʏ ᴅᴀᴅ :<a href=https://t.me/it_was_abhi>ᴀʙʜɪ</a> \n➻ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ :<a href='https://t.me/botsupportx'>ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ</a> \n\n⚜ ꜰᴏʀ ᴀɴɪᴍᴇ ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟꜱ ᴀɴᴅ ɢʀᴏᴜᴘꜱ : \n\n➻ ᴀɴɪᴍᴇ ɪɴ ʜɪɴᴅɪ : <a href='https://t.me/All_Hindi_Anime'>ᴄʟɪᴄᴋ ᴛᴏ ᴊᴏɪɴ</a>\n➻ ᴀɴɪᴍᴇ ꜱᴇʀɪᴇꜱ ʜɪɴᴅɪ : <a href='https://t.me/Anime_In_Hindi_Dub_Only'>ᴄʟɪᴄᴋ ᴛᴏ ᴊᴏɪɴ</a>\n➻ ʙᴜʀᴏᴛᴏ ɪɴ ʜɪɴᴅɪ : <a href='https://t.me/Buroto_In_Hindi_Dub'>ᴄʟɪᴄᴋ ᴛᴏ ᴊᴏɪɴ</a>\n➻ ᴢᴇᴇ ᴄᴀꜰᴇ ɪɴ ʜɪɴᴅɪ :<a href='https://t.me/ZEE_CAFE_HINDI_OFFICIAL'>ᴄʟɪᴄᴋ ᴛᴏ ᴊᴏɪɴ</a>\n\n𝗔𝗡𝗜𝗠𝗘 𝗥𝗜𝗩𝗔𝗟𝗦 ⚡️: <a href='https://t.me/Rivals_Anime_Group'>ᴄʟɪᴄᴋ ᴛᴏ ᴊᴏɪɴ</a>\n𝗔𝗡𝗜𝗠𝗘 𝗔𝗥𝗢𝗫𝗫 ⚡️: <a href='https://t.me/Aroxx_network'>ᴄʟɪᴄᴋ ᴛᴏ ᴊᴏɪɴ</a> \n\nɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ʏᴏᴜʀ ᴏᴡɴ ᴄᴜꜱᴛᴏᴍ ʙᴏᴛ ᴋɪɴᴅʟʏ ᴄᴏɴᴛᴀᴄᴛ <a href=https://t.me/it_was_abhi>ᴍʏ ᴅᴀᴅ</a>"

    START1_TXT = "✨ нєу ʙᴀʙʏ {} 🥀 \n\n➻ ꜱᴏ ʟᴇᴛ ᴍᴇ ᴇxᴘʟᴀɪɴ ɪ ᴀᴍ ᴀɴ ᴀɴᴅᴀᴠᴀɴᴄᴇᴅ ᴘᴏᴡᴇʀꜰᴜʟ ʀᴇɴᴀᴍᴇ ʙᴏᴛ. \n➻ ɪ ᴄᴀɴ ʀᴇɴᴀᴍᴇ ᴀɴᴅ ᴄʜᴀɴɢᴇ ᴛʜᴜᴍʙɴᴀɪʟ ᴏꜰ ʏᴏᴜʀ ꜰɪʟᴇꜱ, ᴠɪᴅᴇᴏꜱ, ᴍᴜꜱɪᴄ, ᴇᴛᴄ.... \n➻ ɪ ᴄᴀɴ ᴀʟꜱᴏ ᴄᴏɴᴠᴇʀᴛ ꜰɪʟᴇ ᴛᴏ ᴠɪᴅᴇᴏ ᴀɴᴅ ᴠɪᴅᴇᴏ ᴛᴏ ꜰɪʟᴇ. \n➻ ɪ ᴀʟꜱᴏ ꜱᴜᴘᴘᴏʀᴛꜱ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ᴀɴᴅ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ. \n\nꜱᴏ ᴛʜᴇ ʙᴏᴛ ɪꜱ ɴᴏᴛ ꜰʀᴇᴇ ɪᴛ'ꜱ ᴘᴀɪᴅ ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴜꜱᴇ ʏᴏᴜ ʜᴀᴠᴇ ᴛᴏ ᴘᴀʏ ᴜꜱ ᴋɪɴᴅʟʏ ᴄᴏɴᴛᴀᴄᴛ ᴜꜱ ʙʏ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ᴄᴏɴᴛᴀᴄᴛ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ꜱᴜʙɪꜱᴄʀɪᴘᴛɪᴏɴ. \n\nꜱᴜʙɪꜱᴄʀɪᴘᴛɪᴏɴ ɪꜱ ʙᴀꜱᴇᴅ ᴏɴ : \n1ᴅᴀʏ - ₹2 \n1ᴍᴏɴᴛʜ - ₹20 \n\nᴡʜʏ ʏᴏᴜ ꜱʜᴏᴜʟᴅ ᴜꜱᴇ ᴛʜɪꜱ ᴘᴀɪᴅ ʙᴏᴛ ɪɴꜱᴛᴇᴀᴅ ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ꜰʀᴇᴇ ʀᴇɴᴀᴍᴇʀ ʙᴏᴛ. \n\n• ᴡᴇ ᴅᴇᴘʟᴏʏᴇᴅ ᴏɴ ᴠᴘꜱ, ꜱᴏ ɪᴛ'ꜱ ꜱᴜᴘᴇʀ ꜰᴀꜱᴛ. \n• ʙᴏᴛ ɪꜱ ᴘʀɪᴠᴀᴛᴇ ꜱᴏ  ʏᴏᴜ ᴡɪʟʟ ɢᴇᴛ ʏᴏᴜʀ 2ɢʙ ꜰɪʟᴇ ɪɴ 1-2 ᴍɪɴꜱ . \n• ɪᴛ'ꜱ ꜱᴏ ᴄʜᴇᴀᴘ ʏᴏᴜ ᴄᴀɴ ᴀꜰꜰᴏʀᴅ ᴇᴀꜱɪʟʏ."

    APK_TXT = "ᴏɴʟʏ ᴄᴏɴᴛᴀᴄᴛ ᴜꜱ ᴛᴏ ɢᴇᴛ ꜱᴜʙɪꜱᴄʀɪᴘᴛɪᴏɴ. \n\n<a href=https://t.me/it_was_abhi>ᴀʙʜɪ</a> \n<a href=https://t.me/Minato_Bruh>ᴍɪɴᴀᴛᴏ</a> \n\nɪꜰ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ Qᴜᴇꜱᴛɪᴏɴꜱ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ᴛʜɪꜱ ʙᴏᴛ ᴋɪɴᴅʟʏ ᴀꜱᴋ <a href=https://t.me/it_was_abhi>ᴍʏ ᴅᴀᴅ</a>"
  
    HELP_TXT = "ᴄʜᴏᴏsᴇ ᴛʜᴇ ᴄᴀᴛᴇɢᴏʀʏ ғᴏʀ ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴɴᴀ ɢᴇᴛ ʜᴇʟᴩ.\nᴀsᴋ ʏᴏᴜʀ ᴅᴏᴜʙᴛs ᴀᴛ [Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ](https://t.me/Botsupportx)\n\nᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : `/`"

    PROGRESS_BAR = """<b>\n 
➻ ᴘʀᴏɢʀᴇss ʙᴀʀ 
» Sɪᴢᴇ: {1} | {2}
» Dᴏɴᴇ : {0}%
» 🚀 Sᴩᴇᴇᴅ: {3}/s
» ⏰️ Eᴛᴀ: {4} </b>"""

    REX_TXT = "✏️ ʜᴏᴡ ᴛᴏ ʀᴇɴᴀᴍᴇ ᴀ ꜰɪʟᴇ  \n\nꜱᴇɴᴅ ᴀɴʏ ꜰɪʟᴇ ᴀɴᴅ ᴛʏᴘᴇ ɴᴇᴡ ꜰɪʟᴇ ɴᴀᴍᴇ. \n\nᴀɴᴅ ꜱᴇʟᴇᴄᴛ ᴛʜᴇ ꜰᴏʀᴍᴀᴛ [ ᴅᴏᴄᴜᴍᴇɴᴛ, ᴠɪᴅᴇᴏ, ᴀᴜᴅɪᴏ ]."
    REX2_TXT = "📑ʜᴏᴡ ᴛᴏ ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ. \n\n/set_caption : ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ꜱᴇᴛ ᴀ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ. \n\n/see_caption : ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴠɪᴇᴡ ʏᴏᴜʀ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ. \n\n/del_caption : ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ. \n\nᴇxᴀᴍᴘʟᴇ -  \n/set_caption 📕 ꜰɪʟᴇ ɴᴀᴍᴇ : {ꜰɪʟᴇɴᴀᴍᴇ} \n💾 ꜱɪᴢᴇ : {ꜰɪʟᴇꜱɪᴢᴇ} \n⏰ ᴅᴜʀᴀᴛɪᴏɴ: {ᴅᴜʀᴀᴛɪᴏɴ}"


    RET_TXT = "🌌ʜᴏᴡ ᴛᴏ ꜱᴇᴛ ᴛʜᴜᴍʙɴᴀɪʟ \n\n/start : ꜱᴇɴᴅ ᴀɴʏ ᴘʜᴏᴛᴏ ᴛᴏ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ꜱᴀᴠᴇ ᴛʜᴜᴍʙɴᴀɪʟ. \n\n/del_thumb : ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴏʟᴅ ᴛʜᴜᴍʙɴᴀɪʟ. \n\n/view_thumb : ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴠɪᴇᴡ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ."
