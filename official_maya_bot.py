from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random
import datetime
from telegram.ext import ApplicationBuilder, JobQueue

# Replace with your bot token
BOT_TOKEN = '8195136794:AAEG1ZRl-JS7p6cFCh87ng_OI31YOAWlAtE'
GIRLFRIEND_CHAT_ID = '123456789'  # Replace with actual chat ID

# Predefined compliments or memories
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

# Daily message handler
async def daily_message(context: ContextTypes.DEFAULT_TYPE):
    message = f"🌼 Good morning, my love!\n\n{random.choice(compliments)}\n\n💭 Memory Lane: {random.choice(memories)}"
    await context.bot.send_message(chat_id=GIRLFRIEND_CHAT_ID, text=message)

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    print(f"Chat ID: {chat_id}")  # Print to terminal
    await update.message.reply_text("Hey love! I’m your daily love bot 💖")


app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

# Schedule daily message at 8 AM
application = ApplicationBuilder().token(BOT_TOKEN).build()
job_queue = app.job_queue
job_queue.run_daily(daily_message, time=datetime.time(hour=8, minute=0))

print("Bot is running...")
app.run_polling()
