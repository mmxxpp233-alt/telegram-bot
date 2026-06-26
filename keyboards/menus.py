from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


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
                )
            ],

            [
                InlineKeyboardButton(
                    text="🔗 اختصار روابط",
                    callback_data="short_link"
                ),
                InlineKeyboardButton(
                    text="🛡️ فحص الروابط",
                    callback_data="check_link"
                )
            ],

            [
                InlineKeyboardButton(
                    text="✨ زخرفة",
                    callback_data="decorate"
                ),
                InlineKeyboardButton(
                    text="🎤 تحويل نص لصوت",
                    callback_data="tts"
                )
            ],

            [
                InlineKeyboardButton(
                    text="📞 أرقام وهمية",
                    callback_data="fake_numbers"
                ),
                InlineKeyboardButton(
                    text="👤 معلوماتك",
                    callback_data="user_info"
                )
            ],

            [
                InlineKeyboardButton(
                    text="🆔 إنشاء يوزر",
                    callback_data="create_username"
                ),
                InlineKeyboardButton(
                    text="👨‍💻 المطور",
                    callback_data="developer"
                )
            ]

        ]
    )
