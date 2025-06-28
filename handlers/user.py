from aiogram import types, Dispatcher
from database import save_user_name, save_birthday, get_user_name
from utils.gemini import chat_with_gemini
from utils.mood import ask_mood

async def start_cmd(message: types.Message):
    name = message.from_user.first_name
    await message.reply(f"Hi {name} 🌸! I'm Mishu..💃🏻, your BFF 🫢\nType anything or use /hug /gif!")

async def hug_cmd(message: types.Message):
    await message.reply("Sending you a warm hug 🤗💕")

async def gif_cmd(message: types.Message):
    await message.reply("Here’s a cute GIF! (You can add random GIF logic here)")

async def setname_cmd(message: types.Message):
    parts = message.text.split(maxsplit=1)
    if len(parts) == 2:
        await save_user_name(message.from_user.id, parts[1])
        await message.reply(f"Got it! I'll call you {parts[1]} 💖")
    else:
        await message.reply("Usage: /setname YourName")

async def birthday_cmd(message: types.Message):
    parts = message.text.split(maxsplit=1)
    if len(parts) == 2:
        await save_birthday(message.from_user.id, parts[1])
        await message.reply("Birthday saved 🎉 I'll remind you!")
    else:
        await message.reply("Usage: /birthday DD-MM")

async def mood_cmd(message: types.Message):
    await ask_mood(message)

async def handle_text(message: types.Message):
    name = await get_user_name(message.from_user.id)
    reply = await chat_with_gemini(message.text, name or message.from_user.first_name)
    await message.reply(reply)

def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(start_cmd, commands=["start"])
    dp.register_message_handler(hug_cmd, commands=["hug"])
    dp.register_message_handler(gif_cmd, commands=["gif"])
    dp.register_message_handler(setname_cmd, commands=["setname"])
    dp.register_message_handler(birthday_cmd, commands=["birthday"])
    dp.register_message_handler(mood_cmd, commands=["mood"])
    dp.register_message_handler(handle_text)
