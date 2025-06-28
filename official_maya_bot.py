from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random
import datetime
import os
import logging

# Enable logging for debugging
logging.basicConfig(level=logging.INFO)

# Use environment variable or hardcoded token (for local testing only)
BOT_TOKEN = os.getenv("BOT_TOKEN", "8195136794:AAEG1ZRl-JS7p6cFCh87ng_OI31YOAWlAtE")
GIRLFRIEND_CHAT_ID = '123456789'  # Replace with actual chat ID

# Predefined compliments and memories
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

# Daily message task
async def daily_message(context: ContextTypes.DEFAULT_TYPE):
    message = (
        f"🌼 Good morning, my love!\n\n"
        f"{random.choice(compliments)}\n\n"
        f"💭 Memory Lane: {random.choice(memories)}"
    )
    await context.bot.send_message(chat_id=GIRLFRIEND_CHAT_ID, text=message)

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    logging.info(f"Chat ID: {chat_id}")  # Logged for easier deployment debugging
    await update.message.reply_text("Hey love! I’m your daily love bot 💖")

# Main app entry
if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Register the command
    app.add_handler(CommandHandler("start", start))

    # Schedule daily message at 8:00 AM
    app.job_queue.run_daily(
        callback=daily_message,
        time=datetime.time(hour=8, minute=0),
        name="daily_love_message"
    )

    logging.info("Bot is running...")
    app.run_polling()
