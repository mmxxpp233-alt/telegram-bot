from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="📷 قراءة باركود", callback_data="barcode_read"),
                InlineKeyboardButton(text="🧾 إنشاء باركود", callback_data="barcode_create")
            ],
            [
                InlineKeyboardButton(text="🔗 فحص الروابط", callback_data="check_link"),
                InlineKeyboardButton(text="🔊 تحويل نص لصوت", callback_data="tts")
            ],
            [
                InlineKeyboardButton(text="✨ زخرفة أسماء", callback_data="decorate_names"),
                InlineKeyboardButton(text="👤 إنشاء يوزر تليجرام", callback_data="gen_user")
            ],
            [
                InlineKeyboardButton(text="🔗 اختصار الروابط", callback_data="short_link"),
                InlineKeyboardButton(text="🤖 إنشاء بوت", callback_data="create_bot")
            ],
            [
                InlineKeyboardButton(text="👨‍💻 المطور", callback_data="developer"),
                InlineKeyboardButton(text="🛡️ حماية IP", callback_data="ip_protect")
            ]
        ]
    )
