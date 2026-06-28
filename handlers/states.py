from aiogram.fsm.state import State, StatesGroup


class BotStates(StatesGroup):

    # =========================
    # 📱 QR
    # =========================
    qr_create = State()
    qr_read = State()

    # =========================
    # 🔗 LINKS
    # =========================
    short_link = State()
    check_link = State()

    # =========================
    # ✨ DECORATION
    # =========================
    decorate_text = State()

    # =========================
    # 🔊 TEXT TO SPEECH
    # =========================
    tts_text = State()

    # =========================
    # 🆔 USERNAME GENERATOR
    # =========================
    username_type = State()

    # =========================
    # 👤 USER INFO (اختياري استخدامه كـ placeholder)
    # =========================
    waiting_input = State()
