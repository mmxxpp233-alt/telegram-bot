from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="📷 QR إنشاء", callback_data="qr_create"),
            InlineKeyboardButton(text="📷 QR قراءة", callback_data="qr_read")
        ],
        [
            InlineKeyboardButton(text="🔗 فحص رابط", callback_data="check_link"),
            InlineKeyboardButton(text="✂️ اختصار رابط", callback_data="short_link")
        ],
        [
            InlineKeyboardButton(text="🔊 تحويل صوت", callback_data="tts"),
            InlineKeyboardButton(text="✨ زخرفة", callback_data="decorate")
        ],
        [
            InlineKeyboardButton(text="👤 معلوماتك", callback_data="user_info"),
            InlineKeyboardButton(text="🛡️ حماية IP", callback_data="ip_protect")
        ],
        [
            InlineKeyboardButton(text="🔙 رجوع", callback_data="back"),
            InlineKeyboardButton(text="👨‍💻 المطور", callback_data="developer")
        ]
    ])
