import os

# Pyrogram API credentials
API_ID = int(os.environ.get("API_ID", '22561857'))
API_HASH = os.environ.get("API_HASH", "6581d3daf4b40f722a22ddb5ca1281c2")

# Bot token
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6663117439:AAG5P6lOxznw-Bh0piw66Jex7pExth4LbdM")

# Pyrogram session name
SESSION_NAME = os.environ.get("SESSION_NAME")

# MongoDB URI (if you're using MongoDB)
MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://aio:aio@aio.5z4gxok.mongodb.net/?retryWrites=true&w=majority")
