import os
from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from services.qr import read_qr

router = Router()


@router.message(F.photo)
async def handle_photo(message: Message, state: FSMContext):

    if await state.get_state() != "qr_wait":
        return

    file = await message.bot.get_file(message.photo[-1].file_id)

    path = f"qr_{message.from_user.id}.png"

    await message.bot.download_file(file.file_path, path)

    result = read_qr(path)

    os.remove(path)

    await state.clear()

    if result:
        await message.answer(f"📄 تم قراءة QR:\n\n{result}")
    else:
        await message.answer("❌ مفيش QR في الصورة")
