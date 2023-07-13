import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
from helper.database import db
from config import Config

@Client.on_message(filters.private & filters.command("start"))
async def start(client, message):
    user = message.from_user
    await db.add_user(client, message)
    
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
    elif data == "apk":
        await query.message.edit_text(
            text=Txt.APK_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data = "close"),
                InlineKeyboardButton("ʙᴀᴄᴋ", callback_data = "start")
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
  
