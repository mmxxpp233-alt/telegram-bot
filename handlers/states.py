from aiogram.fsm.state import State, StatesGroup


class BotStates(StatesGroup):

    # ================= QR =================
    qr_create = State()
    qr_read = State()

    # ================= Links =================
    short_link = State()
    check_link = State()

    # ================= Decoration =================
    decorate_type = State()
    decorate_text = State()

    # ================= Text To Speech =================
    tts_gender = State()
    tts_text = State()

    # ================= Username Generator =================
    username_type = State()

    # ================= General =================
    waiting_input = State()
