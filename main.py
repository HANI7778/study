from pyrogram import Client, filters

API_ID=""
API_HASH=""
BOT_TOKEN=""


SPIDEYTOM = Client(
    name="PyrogramBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

print("Bot Started")
SPIDEYTOM.run()
