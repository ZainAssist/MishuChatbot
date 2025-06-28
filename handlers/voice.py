from aiogram import types, Dispatcher

async def handle_voice(message: types.Message):
    await message.reply("I received your voice 🎤 but I'm still learning to understand audio!")

def register_voice_handlers(dp: Dispatcher):
    dp.register_message_handler(handle_voice, content_types=types.ContentType.VOICE)
