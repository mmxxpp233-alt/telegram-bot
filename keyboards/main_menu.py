from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)


def main_menu():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📷 إنشاء QR",
                    callback_data="qr"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🎨 زخرفة النص",
                    callback_data="decorate"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🔊 تحويل النص لصوت",
                    callback_data="tts"
                )
            ],
            [
                InlineKeyboardButton(
                    text="👤 مولد يوزرات",
                    callback_data="username"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📱 أرقام وهمية",
                    callback_data="fake_numbers"
                )
            ],
            [
                InlineKeyboardButton(
                    text="ℹ️ المطور",
                    callback_data="developer"
                )
            ],
        ]
    )

    return keyboard
