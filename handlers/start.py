from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📢 قناة 1", url="https://t.me/feraon_1")],
        [InlineKeyboardButton("📢 قناة 2", url="https://t.me/my_botg1")],
        [InlineKeyboardButton("📢 قناة 3", url="https://t.me/fraon10k")],
        [InlineKeyboardButton("✅ تحقق", callback_data="check")]
    ])

async def start_handler(update, context):
    from config import HEADER_IMAGE, JOIN_MESSAGE

    await update.message.reply_photo(
        photo=HEADER_IMAGE,
        caption=JOIN_MESSAGE,
        reply_markup=keyboard()
    )
