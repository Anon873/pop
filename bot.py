from datetime import datetime
from pytz import timezone
from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from config import Config
from aiohttp import web
from route import web_server

class Bot(Client):

    def __init__(self):
        super().__init__(
            name="renamer",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            workers=200,
            plugins={"root": "plugins"},
            sleep_threshold=15,
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.mention = me.mention
        self.username = me.username  
        self.uptime = Config.BOT_UPTIME     
        if Config.WEBHOOK:
            app = web.AppRunner(await web_server())
            await app.setup()       
            await web.TCPSite(app, "0.0.0.0", 8080).start()     
        print(f"{me.first_name} ɪꜱ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴜᴘᴅᴀᴛᴇᴅ ᴡɪᴛʜ ɴᴇᴡ ᴠᴇʀꜱɪᴏɴ ᴀɴᴅ ꜱᴛᴀʀᴛᴇᴅ.....✨")
        for id in Config.ADMIN:
            try: await self.send_message(id, f"**__{me.first_name}  ɪꜱ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴜᴘᴅᴀᴛᴇᴅ ᴡɪᴛʜ ɴᴇᴡ ᴠᴇʀꜱɪᴏɴ ᴀɴᴅ ꜱᴛᴀʀᴛᴇᴅ.....✨__**")                                
            except: pass
        if Config.LOG_CHANNEL:
            try:
                curr = datetime.now(timezone("Asia/Kolkata"))
                date = curr.strftime('%d %B, %Y')
                time = curr.strftime('%I:%M:%S %p')
                await self.send_message(Config.LOG_CHANNEL, f"**__{me.mention} ꜱᴜᴄᴇꜱꜱꜰᴜʟʟʏ ʀᴇꜱᴛᴀʀᴛᴇᴅ !!!**\n\n📅 ᴅᴀᴛᴇ : `{date}`\n⏰ ᴛɪᴍᴇ : `{time}`\n🌐 ᴛɪᴍᴇᴢᴏɴᴇ : `Asia/Kolkata`\n\n🉐 ᴠᴇʀꜱɪᴏɴ : `v{__version__} (Layer {layer})`</b>")                                
            except:
                print("ᴘʟᴇᴀꜱᴇ ᴍᴀᴋᴇ ᴛʜᴇ ʙᴏᴛ ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ʟᴏɢ ᴄʜᴀɴɴᴇʟ.")

await Bot().run()
