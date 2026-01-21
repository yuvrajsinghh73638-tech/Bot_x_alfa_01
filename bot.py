import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "8529180151:AAES7AWR818cGYCd_DA3SrK4AE7ATcwR6_o"

if not BOT_TOKEN:
    raise ValueError("Bot Token nahi mila!")

app = ApplicationBuilder().token(BOT_TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is running!")

app.add_handler(CommandHandler("start", start))

app.run_polling()


