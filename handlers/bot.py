# Main bot logic (Pyrogram)

from pyrogram import Client, filters
from config import *

app = Client("bff_bot", mongo_uri=MONGO_URI, gemini_api_key=GEMINI_API_KEY, log_channel_id=LOG_CHANNEL_ID, bot_token=BOT_TOKEN)

@app.on_message(filters.private & filters.text)
def chat_handler(client, message):
    message.reply_text("Hey Mishu! 💖 I'm here for you always.")

app.run()
