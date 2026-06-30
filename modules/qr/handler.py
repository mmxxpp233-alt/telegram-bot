import io

from aiogram import Router, F
from aiogram.types import (
    CallbackQuery,
    Message,
    BufferedInputFile,
)
from aiogram.fsm.context import FSMContext

from modules.qr.state import QRState
from modules.qr.service import generate_qr

router = Router()


@router.callback_query(F.data == "qr_create")
async def qr_create(call: CallbackQuery, state: FSMContext):

    await state.set_state(QRState.waiting_for_text)

    await call.message.answer(
        "📱 أرسل الآن النص أو الرابط الذي تريد تحويله إلى QR."
    )

    await call.answer()
    @router.message(QRState.waiting_for_text)
async def receive_qr_text(message: Message, state: FSMContext):

    text = message.text.strip()

    qr_buffer = generate_qr(text)

    qr_bytes = qr_buffer.read()

    qr_file = BufferedInputFile(
        qr_bytes,
        filename="qr_code.png"
    )

    await message.answer_document(
        document=qr_file,
        caption="✅ تم إنشاء رمز QR بنجاح."
    )

    await state.clear()
