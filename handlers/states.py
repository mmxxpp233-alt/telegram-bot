from aiogram.fsm.state import State, StatesGroup


class BotStates(StatesGroup):

    # 📷 QR
    qr_create = State()
    qr_read = State()

    # 🔗 روابط
    link_check = State()
    short_link = State()

    # 🔊 تحويل صوت
    tts_type = State()
    tts_text = State()

    # ✨ زخرفة
    decorate = State()

    # 👤 user / system (اختياري للمستقبل)
    waiting_input = State()
