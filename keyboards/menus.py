from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📱 رقم جديد",
                    callback_data="new_number"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🔊 تحويل نص لصوت",
                    callback_data="tts"
                ),
                InlineKeyboardButton(
                    text="✨ زخرفة",
                    callback_data="decorate"
                )
            ]
        ]
    )
