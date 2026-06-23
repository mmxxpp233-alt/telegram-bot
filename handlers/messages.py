from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[

        # 1 - QR قراءة
        [
            InlineKeyboardButton(text="📷 قراءة QR", callback_data="qr_read")
        ],

        # 2 - QR إنشاء
        [
            InlineKeyboardButton(text="🧾 إنشاء QR", callback_data="qr_create")
        ],

        # 3 - فحص روابط
        [
            InlineKeyboardButton(text="🔗 فحص الروابط", callback_data="check_link")
        ],

        # 4 - تحويل نص لصوت
        [
            InlineKeyboardButton(text="🔊 تحويل نص لصوت", callback_data="tts")
        ],

        # 5 - زخرفة أسماء
        [
            InlineKeyboardButton(text="✨ زخرفة الأسماء", callback_data="decorate")
        ],

        # 6 - إنشاء يوزر تيليجرام
        [
            InlineKeyboardButton(text="👤 إنشاء يوزر", callback_data="new_user")
        ],

        # 7 - اختصار الروابط
        [
            InlineKeyboardButton(text="✂️ اختصار الروابط", callback_data="short_link")
        ],

        # 8 - إنشاء بوت
        [
            InlineKeyboardButton(text="🤖 إنشاء بوت", callback_data="create_bot")
        ],

        # 9 - المطور
        [
            InlineKeyboardButton(text="👨‍💻 المطور", callback_data="developer")
        ],

        # 10 - حماية IP
        [
            InlineKeyboardButton(text="🛡️ حماية IP", callback_data="ip_protect")
        ],

        # إضافات احترافية
        [
            InlineKeyboardButton(text="ℹ️ شرح البوت", callback_data="info"),
            InlineKeyboardButton(text="⚙️ الإعدادات", callback_data="settings")
        ]
    ])
