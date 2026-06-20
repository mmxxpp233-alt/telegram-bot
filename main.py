from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import BOT_TOKEN

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 أهلاً بيك في البوت الاحترافي\n\n"
        "استخدم الأمر:\n"
        "/info @username"
    )

# /info
async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❌ اكتب اليوزر بعد الأمر\nمثال: /info @telegram")
        return

    username = context.args[0]

    try:
        chat = await context.bot.get_chat(username)

        name = chat.first_name or "N/A"

        bio = getattr(chat, "bio", "N/A")

        text = (
            f"👤 الاسم: {name}\n"
            f"🔗 اليوزر: {username}\n"
            f"📝 Bio: {bio}"
        )

        await update.message.reply_text(text)

        # صورة البروفايل
        photos = await context.bot.get_user_profile_photos(chat.id)

        if photos.total_count > 0:
            photo = photos.photos[0][-1].file_id
            await context.bot.send_photo(update.effective_chat.id, photo)

    except Exception:
        await update.message.reply_text("⚠️ المستخدم غير موجود أو الحساب خاص")

# تشغيل البوت
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("info", info))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
