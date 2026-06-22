from aiogram import Router, F
from aiogram.fsm.context import FSMContext

router = Router()


@router.callback_query(F.data == "barcode_read")
async def barcode_read(call, state: FSMContext):

    await state.set_state("qr_wait")

    await call.answer()

    await call.message.answer("📷 ابعت صورة فيها QR Code")
