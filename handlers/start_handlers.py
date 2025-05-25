from telegram import Update
from telegram.ext import ContextTypes

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Namaste {update.effective_user.first_name}!\n\nMain active ho chuka hoon. Kisi bhi command ke liye ya madad ke liye mujhe message bhejiye."
    )
