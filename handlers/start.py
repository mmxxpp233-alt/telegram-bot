from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes
from config import HEADER_IMAGE, JOIN_MESSAGE, CHANNELS


def keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📢 قناة 1", url=CHANNELS[0])],
        [InlineKeyboardButton("📢 قناة 2", url=CHANNELS[1])],
        [InlineKeyboardButton("📢 قناة 3", url=CHANNELS[2])],
        [InlineKeyboardButton("✅ تحقق", callback_data="check")]
    ])


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.reply_photo(
            photo=HEADER_IMAGE,
            caption=JOIN_MESSAGE,
            reply_markup=keyboard()
        )
