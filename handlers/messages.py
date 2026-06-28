from aiogram import Router, F
from aiogram.types import CallbackQuery

router = Router()

async def not_ready(call: CallbackQuery, title: str):
await call.answer()

await call.message.answer(
    f"""🚧 {title}

❌ هذه الميزة لم تتم إضافتها بعد.

⏳ سيتم تفعيلها قريبًا."""
)

==========================

QR

==========================

@router.callback_query(F.data == "qr_create")
async def qr_create(call: CallbackQuery):
await not_ready(call, "📱 إنشاء QR")

@router.callback_query(F.data == "qr_read")
async def qr_read(call: CallbackQuery):
await not_ready(call, "📷 قراءة QR")

==========================

Links

==========================

@router.callback_query(F.data == "short_link")
async def short_link(call: CallbackQuery):
await not_ready(call, "🔗 اختصار الروابط")

@router.callback_query(F.data == "check_link")
async def check_link(call: CallbackQuery):
await not_ready(call, "🛡️ فحص الروابط")
