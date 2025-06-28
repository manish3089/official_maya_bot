from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random
import datetime
import os
import logging
import pytz

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")
GIRLFRIEND_CHAT_ID = os.getenv("GIRLFRIEND_CHAT_ID")  # Set this in Render

compliments = [
    "You're my sunshine on cloudy days ☀️",
    "Every moment with you is a treasure 🥰",
    "I still get butterflies when I see your name pop up 💌",
    "You're not just my love, you're my best friend 💕",
]

memories = [
    "Remember that rainy walk we had on our first date? I’ll never forget it. 🌧️❤️",
    "The first time I saw you laugh so hard, I knew I was falling. 😂💖",
    "That coffee shop moment where you said something silly and we both laughed for 5 minutes ☕",
]

async def daily_message(context: ContextTypes.DEFAULT_TYPE):
    message = (
        f"🌼 Good morning, my love!\n\n"
        f"{random.choice(compliments)}\n\n"
        f"💭 Memory Lane: {random.choice(memories)}"
    )
    await context.bot.send_message(chat_id=GIRLFRIEND_CHAT_ID, text=message)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    logging.info(f"User started the bot. Chat ID: {chat_id}")
    await update.message.reply_text("Hey love! I’m your daily love bot 💖")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    # 8 AM IST = 2:30 AM UTC
    app.job_queue.run_daily(
        callback=daily_message,
        time=datetime.time(hour=2, minute=30, tzinfo=datetime.timezone.utc),
        name="daily_love_message"
    )
    logging.info("Bot is running...")
    app.run_polling()
