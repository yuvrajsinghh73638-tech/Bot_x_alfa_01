import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# 8529180151:AAES7AWR818cGYCd_DA3SrK4AE7ATcwR6_o
BOT_TOKEN = "8529180151:AAES7AWR818cGYCd_DA3SrK4AE7ATcwR6_o"

# Is line mein bracket ke andar BOT_TOKEN hi rahega
app = ApplicationBuilder().token(BOT_TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is running!")

app.add_handler(CommandHandler("start", start))

if __name__ == "__main__":
    app.run_polling()
    
