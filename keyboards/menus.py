from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔊 تحويل لصوت", callback_data="tts")],
        [InlineKeyboardButton(text="✨ زخرفة", callback_data="decorate")],
        [InlineKeyboardButton(text="🔗 فحص رابط", callback_data="check_link")],
        [InlineKeyboardButton(text="📷 إنشاء QR", callback_data="qr_create")],
        [InlineKeyboardButton(text="📷 قراءة QR", callback_data="qr_read")],

        [InlineKeyboardButton(text="🌐 اختصار روابط", callback_data="short_link")],
        [InlineKeyboardButton(text="👤 إنشاء يوزر", callback_data="user_gen")],
        [InlineKeyboardButton(text="🤖 إنشاء بوت", callback_data="bot_create")],
        [InlineKeyboardButton(text="👨‍💻 المطور", callback_data="dev")],
        [InlineKeyboardButton(text="🛡 حماية IP", callback_data="ip_protect")],
    ])
