import asyncio

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN

# Handlers
from handlers.start import router as start_router
from handlers.subscription import router as subscription_router
