from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[

        [
            InlineKeyboardButton(text="📷 قراءة QR", callback_data="qr_read"),
            InlineKeyboardButton(text="🧾 إنشاء QR", callback_data="qr_create")
        ],

        [
            InlineKeyboardButton(text="🔗 فحص الروابط", callback_data="check_link"),
            InlineKeyboardButton(text="✂️ اختصار الروابط", callback_data="short_link")
        ],

        [
            InlineKeyboardButton(text="🔊 تحويل لصوت", callback_data="tts"),
            InlineKeyboardButton(text="✨ زخرفة", callback_data="decorate")
        ],

        [
            InlineKeyboardButton(text="👤 إنشاء يوزر", callback_data="new_user"),
            InlineKeyboardButton(text="🤖 إنشاء بوت", callback_data="create_bot")
        ],

        [
            InlineKeyboardButton(text="👨‍💻 المطور", callback_data="developer"),
            InlineKeyboardButton(text="🛡️ حماية IP", callback_data="ip_protect")
        ],

        [
            InlineKeyboardButton(text="ℹ️ معلومات", callback_data="info"),
            InlineKeyboardButton(text="⚙️ الإعدادات", callback_data="settings")
        ]
    ])
