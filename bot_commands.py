from aiogram import Bot
from aiogram.types import BotCommand


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="🚀 تشغيل البوت"),
        BotCommand(command="how_to_use", description="📖 شرح استخدام البوت"),
        BotCommand(command="chat_cleanup", description="🧹 تنظيف الشات"),
    ]

    await bot.set_my_commands(commands)
