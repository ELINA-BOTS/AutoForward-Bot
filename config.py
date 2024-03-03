import os

# Pyrogram API credentials
API_ID = int(os.environ.get("API_ID", '22561857'))
API_HASH = os.environ.get("API_HASH", "6581d3daf4b40f722a22ddb5ca1281c2")

# Bot token
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6558508467:AAE71Fy7bWSpD-2qd-LPH9tAnL2GW8T1Qe4")

# Pyrogram session name
SESSION_NAME = os.environ.get("SESSION_NAME")

# MongoDB URI (if you're using MongoDB)
MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://aio:aio@aio.5z4gxok.mongodb.net/?retryWrites=true&w=majority")
