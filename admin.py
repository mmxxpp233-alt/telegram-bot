from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.markdown import text

router = Router()

# 🔐 قائمة الـ Admins
ADMIN_IDS = [7771042305, 123456789]  # ضع IDs أكثر من واحد

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
    if message.from_user.id not in ADMIN_IDS:
        return  # ما يظهرش لغير الأدمن

    await message.answer("🛡️ لوحة التحكم السرية", reply_markup=admin_panel())


# 📢 أمر للرسالة الجماعية
@router.callback_query(F.data == "admin_broadcast")
async def broadcast_message(call):
    if call.from_user.id not in ADMIN_IDS:
        await call.answer("❌ ليس لديك صلاحية", show_alert=True)
        return

    await call.message.answer("📝 أرسل لي نص الرسالة الجماعية التي تريد تحويلها لصوت.")


@router.message(F.text)  # استقبل أي نص بعد
async def handle_broadcast_text(message: Message):
    if message.from_user.id not in ADMIN_IDS:
        return

    # هنا حول النص لصوت وأرسله (هذه الخطوة تحتاج مكتبة تحويل النص لصوت)
    # مثال: استخدم مكتبة TTS مثل gTTS أو أي خدمة أخرى
    # ثم أرسل الملف الصوتي للغروب أو القناة المحددة
    await message.answer("تم استلام الرسالة، جاري تحويلها وإرسالها.")


# باقي الكود زي ما هو (الأزرار الثانية)
