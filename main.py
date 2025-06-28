from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from config import BOT_TOKEN
from handlers.user import register_user_handlers
from handlers.admin import register_admin_handlers
from handlers.voice import register_voice_handlers

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Register all handlers
register_user_handlers(dp)
register_admin_handlers(dp)
register_voice_handlers(dp)

async def on_startup(_):
    print("Mishu Chat Bot is online!")

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
