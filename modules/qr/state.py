from aiogram.fsm.state import State, StatesGroup


class QRState(StatesGroup):
    waiting_for_text = State()
