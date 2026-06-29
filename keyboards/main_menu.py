from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import (
    DEVELOPER_USERNAME,
    BOT_MAKER_USERNAME,
    FAKE_NUMBERS_URL,
)


def main_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📱 إنشاء QR",
                    callback_data="qr_create"
                ),
                InlineKeyboardButton(
                    text="📷 قراءة QR",
                    callback_data="qr_read"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔗 اختصار روابط",
                    callback_data="short_link"
                ),
                InlineKeyboardButton(
                    text="🛡️ فحص الروابط",
                    callback_data="check_link"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="✨ زخرفة النص",
                    callback_data="decorate"
                ),
                InlineKeyboardButton(
                    text="🔊 تحويل نص لصوت",
                    callback_data="tts"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="👤 معلوماتك",
                    callback_data="user_info"
                ),
                InlineKeyboardButton(
                    text="🆔 إنشاء يوزر",
                    callback_data="username"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="📲 أرقام وهمية",
                    url=FAKE_NUMBERS_URL
                ),
                InlineKeyboardButton(
                    text="🤖 صانع البوتات",
                    url=f"https://t.me/{BOT_MAKER_USERNAME.lstrip('@')}"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="👨‍💻 المبرمج",
                    url=f"https://t.me/{DEVELOPER_USERNAME.lstrip('@')}"
                ),
            ],
        ]
    )
