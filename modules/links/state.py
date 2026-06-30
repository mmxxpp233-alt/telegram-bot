from aiogram.fsm.state import State, StatesGroup


class LinkState(StatesGroup):
    waiting_for_link = State()
