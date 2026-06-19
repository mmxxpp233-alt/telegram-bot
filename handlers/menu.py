from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from config import MENU_IMAGE, OWNER_USERNAME


def menu_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📱 الحصول على رقم", callback_data="get_number")],
        [InlineKeyboardButton("📜 الشروط", callback_data="rules")]
    ])


async def show_menu(update):
    await update.message.reply_photo(
        photo=MENU_IMAGE,
        caption=f"🏠 اللوحة الرئيسية\n👨‍💻 المطور: {OWNER_USERNAME} 🟦",
        reply_markup=menu_keyboard()
    )


async def menu_handler(update, context):
    query = update.callback_query
    await query.answer()

    await query.message.reply_photo(
        photo=MENU_IMAGE,
        caption=f"🏠 اللوحة الرئيسية\n👨‍💻 المطور: {OWNER_USERNAME} 🟦",
        reply_markup=menu_keyboard()
    )
