from aiogram import Router, F
from aiogram.types import Message

router = Router()


# 📖 شرح البوت
@router.message(F.text == "/how_to_use")
async def how_to_use(message: Message):
    await message.answer(
        "📖 شرح استخدام البوت:\n\n"
        "🔹 استخدم الأزرار في القائمة\n"
        "🔹 اختر الخدمة المطلوبة\n"
        "🔹 كل الخدمات تعمل بشكل مباشر\n\n"
        "🚀 استمتع باستخدام البوت"
    )


# 🧹 تنظيف الشات
@router.message(F.text == "/chat_cleanup")
async def chat_cleanup(message: Message):
    await message.answer("🧹 تم طلب تنظيف الشات\n\n⚠️ ملاحظة: Telegram لا يسمح للبوت بحذف كل المحادثة تلقائيًا، لكن تم تسجيل الأمر.")
