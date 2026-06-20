from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import BOT_TOKEN

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 أهلاً بيك!\n\n"
        "ابعت الأمر بالشكل ده:\n"
        "/info @username"
    )

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❌ اكتب اليوزر بعد الأمر")
        return

    username = context.args[0]

    try:
        user = await context.bot.get_chat(username)

        name = user.first_name or "N/A"
        bio = user.bio if hasattr(user, "bio") else "N/A"

        text = f"""
👤 الاسم: {name}
🔗 اليوزر: {username}
📝 Bio: {bio}
"""

        await update.message.reply_text(text)

        # صورة البروفايل
        photos = await context.bot.get_user_profile_photos(user.id)

        if photos.total_count > 0:
            photo_file = photos.photos[0][-1].file_id
            await context.bot.send_photo(update.effective_chat.id, photo_file)

    except Exception:
        await update.message.reply_text("⚠️ لم يتم العثور على المستخدم أو الحساب خاص")

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("info", info))

    print("Bot is running...")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
