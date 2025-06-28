from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random
import datetime
import os
import logging
import pytz

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "8195136794:AAEG1ZRl-JS7p6cFCh87ng_OI31YOAWlAtE"
GIRLFRIEND_CHAT_ID = '7719180775'  # Set this in Render

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
    birthday_message = (
        "🎉 Happy Birthday, my love! 🎂\n\n"
        "This little bot is my surprise gift to you — it'll send you love, smiles, and memories every single day 💖\n\n"
        "You mean the world to me, and I wanted something special that lasts beyond just today.\n\n"
        "Let's begin your daily love letters ❤️"
    )
    
    await update.message.reply_text(birthday_message)

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
