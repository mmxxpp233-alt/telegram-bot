from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🔊 تحويل نص لصوت", callback_data="tts"),
                InlineKeyboardButton(text="✨ زخرفة", callback_data="decorate")
            ],
            [
                InlineKeyboardButton(text="🔗 فحص رابط", callback_data="check_link"),
                InlineKeyboardButton(text="📊 معلومات", callback_data="info")
            ],
            [
                InlineKeyboardButton(text="⚙️ إعدادات", callback_data="settings")
            ]
        ]
    )
