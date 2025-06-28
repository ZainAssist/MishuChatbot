from aiogram import types, Dispatcher
from config import ADMIN_ID
from database import get_user_count, get_all_users
from aiogram.dispatcher.filters import Command

async def stats_cmd(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        return
    count = await get_user_count()
    await message.reply(f"Total users: {count}")

async def broadcast_cmd(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        return
    text = message.text.split(maxsplit=1)
    if len(text) < 2:
        await message.reply("Usage: /broadcast Your message")
        return

    users = await get_all_users()
    for user in users:
        try:
            await message.bot.send_message(user, text[1])
        except:
            continue
    await message.reply("Broadcast sent ✅")

def register_admin_handlers(dp: Dispatcher):
    dp.register_message_handler(stats_cmd, commands=["stats"])
    dp.register_message_handler(broadcast_cmd, commands=["broadcast"])
