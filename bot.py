import telebot
from telebot import types
import json
import os

TOKEN = "8208644401:AAFc4JM2nX7hp11r6zqQqFShwC6U6rIvmtg"
ADMIN_ID =  7771042305 # حط ايديك هنا

bot = telebot.TeleBot(TOKEN)

DATA_FILE = "data.json"

# ================= DATA =================
def load_data():
    if not os.path.exists(DATA_FILE):
        return {
            "maintenance": False,
            "vodafone_cash": "",
            "countries": {}
        }
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

data = load_data()

# ================= CHECK ADMIN =================
def is_admin(user_id):
    return user_id == ADMIN_ID

# ================= MAIN MENU =================
def main_menu():
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton("📦 الدول", callback_data="countries"))
    kb.add(types.InlineKeyboardButton("💳 الدفع", callback_data="pay"))
    return kb

# ================= ADMIN PANEL =================
def admin_panel():
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton("➕ إضافة دولة", callback_data="add_country"))
    kb.add(types.InlineKeyboardButton("❌ حذف دولة", callback_data="del_country"))
    kb.add(types.InlineKeyboardButton("📱 إضافة رقم", callback_data="add_number"))
    kb.add(types.InlineKeyboardButton("💰 فودافون كاش", callback_data="set_voda"))
    kb.add(types.InlineKeyboardButton("🔧 صيانة ON/OFF", callback_data="maint"))
    return kb

# ================= START =================
@bot.message_handler(commands=["start"])
def start(message):

    if data["maintenance"] and not is_admin(message.from_user.id):
        bot.send_message(message.chat.id, "🔧 البوت في صيانة")
        return

    if is_admin(message.from_user.id):
        bot.send_message(message.chat.id, "🛠 لوحة الأدمن", reply_markup=admin_panel())
    else:
        bot.send_message(message.chat.id, "👋 أهلاً بك في المتجر", reply_markup=main_menu())

# ================= CALLBACK =================
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    global data

    uid = call.from_user.id

    # ================= USER PART =================
    if call.data == "countries":
        kb = types.InlineKeyboardMarkup()

        if not data["countries"]:
            kb.add(types.InlineKeyboardButton("❌ لا يوجد دول", callback_data="none"))
        else:
            for c in data["countries"]:
                kb.add(types.InlineKeyboardButton(c, callback_data=f"c_{c}"))

        bot.edit_message_text("📦 اختر الدولة:", call.message.chat.id, call.message.message_id, reply_markup=kb)

    elif call.data.startswith("c_"):
        c = call.data[2:]
        nums = data["countries"][c]["numbers"]

        text = f"📱 أرقام {c}:\n\n"
        for i, n in enumerate(nums):
            text += f"{i+1}) {n['number']}\n💳 السعر: {n['price']}$\n📌 النوع: {n['type']}\n\n"

        kb = types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton("🛒 شراء", callback_data=f"buy_{c}"))

        bot.send_message(call.message.chat.id, text, reply_markup=kb)

    elif call.data.startswith("buy_"):
        vod = data["vodafone_cash"]

        bot.send_message(
            call.message.chat.id,
            f"💳 الدفع فودافون كاش:\n\nرقم التحويل: {vod}\n\n📸 بعد الدفع ابعت صورة التحويل للأدمن للمراجعة."
        )

    # ================= ADMIN CHECK =================
    if not is_admin(uid):
        return

    if call.data == "add_country":
        msg = bot.send_message(call.message.chat.id, "اكتب اسم الدولة:")
        bot.register_next_step_handler(msg, add_country)

    elif call.data == "del_country":
        msg = bot.send_message(call.message.chat.id, "اكتب اسم الدولة للحذف:")
        bot.register_next_step_handler(msg, del_country)

    elif call.data == "add_number":
        msg = bot.send_message(call.message.chat.id,
        "اكتب: الدولة - الرقم - السعر - النوع")
        bot.register_next_step_handler(msg, add_number)

    elif call.data == "set_voda":
        msg = bot.send_message(call.message.chat.id, "اكتب رقم فودافون كاش:")
        bot.register_next_step_handler(msg, set_voda)

    elif call.data == "maint":
        data["maintenance"] = not data["maintenance"]
        save_data()
        bot.send_message(call.message.chat.id, f"🔧 الصيانة: {data['maintenance']}")

# ================= ADMIN FUNCTIONS =================
def add_country(message):
    data["countries"][message.text] = {"numbers": []}
    save_data()
    bot.send_message(message.chat.id, "✔ تم إضافة الدولة")

def del_country(message):
    if message.text in data["countries"]:
        del data["countries"][message.text]
        save_data()
        bot.send_message(message.chat.id, "✔ تم الحذف")
    else:
        bot.send_message(message.chat.id, "❌ غير موجود")

def add_number(message):
    try:
        c, num, price, typ = message.text.split("-")
        c = c.strip()

        data["countries"][c]["numbers"].append({
            "number": num.strip(),
            "price": price.strip
