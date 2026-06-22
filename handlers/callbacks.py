from aiogram import Router, F

router = Router()


@router.callback_query(F.data == "new_number")
async def new_number(call):
    await call.answer()

    await call.message.answer(
        "📱 زر رقم جديد جاهز للتطوير لاحقًا"
    )


@router.callback_query(F.data == "tts")
async def tts(call):
    await call.answer()

    await call.message.answer(
        "🔊 ميزة تحويل النص لصوت سيتم إضافتها لاحقًا"
    )


@router.callback_query(F.data == "decorate")
async def decorate(call):
    await call.answer()

    await call.message.answer(
        "✨ ميزة الزخرفة سيتم إضافتها لاحقًا"
    )
