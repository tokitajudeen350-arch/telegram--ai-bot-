import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
import datetime

# ====== YOUR BOT SETTINGS ======
BOT_TOKEN = "7804451369:AAFg414rGv-vaU1YUYacUI2IJ17OBF4AfL0"
OWNER_CHAT_ID = 7860619144
# ===============================

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# ====== START COMMAND ======
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 Welcome to Toki Super Trading Bot!\n"
        "I will send Buy/Sell signals with entry time.\n"
        "Type /signal to get an instant signal."
    )

# ====== GENERATE SIGNAL ======
def generate_signal():
    # Here you can connect to Pocket Option API later
    # For now it generates random Buy/Sell signals

    import random
    signal = random.choice(["BUY", "SELL"])
    entry_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return signal, entry_time

# ====== COMMAND TO SEND SIGNAL ======
async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    signal, entry_time = generate_signal()

    message = (
        f"📊 *NEW SIGNAL ALERT*\n\n"
        f"📉 Signal: *{signal}*\n"
        f"⏰ Entry Time: *{entry_time}*\n"
        f"⚡ Market: Forex\n\n"
        f"Use proper risk management."
    )

    await update.message.reply_text(message, parse_mode="Markdown")

# ====== SECRET COMMAND (ONLY YOU) ======
async def owner(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat_id != OWNER_CHAT_ID:
        return

    await update.message.reply_text("Hello Owner, your bot is running perfectly.")

# ====== MAIN BOT FUNCTION ======
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("signal", signal))
    app.add_handler(CommandHandler("owner", owner))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
