from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

router = Router()


class QRState(StatesGroup):
    waiting = State()


@router.callback_query(F.data == "barcode_read")
async def barcode_read(call, state: FSMContext):

    await state.set_state(QRState.waiting)

    await call.answer()

    await call.message.answer("📷 ابعت صورة فيها QR Code")
