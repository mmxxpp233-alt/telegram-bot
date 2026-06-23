import os

# 🔑 توكن البوت (من Railway Variables)
BOT_TOKEN = os.getenv("BOT_TOKEN")

# 🤖 اسم البوت
BOT_NAME = os.getenv("BOT_NAME", "My Bot")

# 🖼️ صورة القائمة الرئيسية
START_IMAGE = os.getenv("START_IMAGE")

# 🛑 صورة الاشتراك الإجباري
SUB_IMAGE = os.getenv("SUB_IMAGE")

# 📢 قنوات الاشتراك الإجباري
CHANNELS = [
    "@feraon_1",
    "@my_botg1",
    "@fraon10k"
]
