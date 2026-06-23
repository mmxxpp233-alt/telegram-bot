from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

# 🔐 حط الـ ID بتاعك هنا
ADMIN_ID = 123456789


def admin_panel():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="📊 الإحصائيات", callback_data="admin_stats")
        ],
        [
            InlineKeyboardButton(text="📢 رسالة جماعية", callback_data="admin_broadcast")
        ],
        [
            InlineKeyboardButton(text="⚙️ إدارة البوت", callback_data="admin_bot")
        ],
        [
            InlineKeyboardButton(text="🔙 إغلاق", callback_data="close_admin")
        ]
    ])


# 🔥 أمر سري للأدمن فقط
@router.message(F.text == "/panel")
async def open_panel(message: Message):

    # 👇 حماية كاملة
    if message.from_user.id != ADMIN_ID:
        return  # ما يظهرش أي حاجة لغيرك

    await message.answer("🛡️ لوحة التحكم السرية", reply_markup=admin_panel())
