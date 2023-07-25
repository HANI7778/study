from pyrogram import Client, filters

API_ID="28347795"
API_HASH="ca929cb8221a920471a3e530c8d72ca9"
BOT_TOKEN=""


SPIDEYTOM = Client(
    name="PyrogramBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

print("Bot Started")
SPIDEYTOM.run()
