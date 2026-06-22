import os
from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from services.qr import read_qr

router = Router()


@router.message(F.photo)
async def handle_photo(message: Message, state: FSMContext):

    # نتأكد إن المستخدم داخل وضع QR فقط
    if await state.get_state() != "qr_wait":
        return

    # تحميل الصورة من تيليجرام
    file = await message.bot.get_file(message.photo[-1].file_id)

    path = f"qr_{message.from_user.id}.png"

    await message.bot.download_file(file.file_path, path)

    # قراءة QR
    result = read_qr(path)

    # حذف الصورة بعد الاستخدام
    os.remove(path)

    # إنهاء الحالة
    await state.clear()

    # الرد على المستخدم
    if result:
        await message.answer(f"📄 تم قراءة QR Code:\n\n{result}")
    else:
        await message.answer("❌ الصورة لا تحتوي على QR Code")
