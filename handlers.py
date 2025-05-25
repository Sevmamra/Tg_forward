from telegram import Update
from telegram.ext import ContextTypes
import logging

logger = logging.getLogger(__name__)

# /start command handler
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    logger.info(f"User {user.id} used /start")
    await update.message.reply_text(f"Hello {user.first_name}! Welcome to the bot.")

# /help command handler
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f"User {update.effective_user.id} used /help")
    await update.message.reply_text("Available commands:\n/start - Start the bot\n/help - Show this help message.")

# Text message handler
async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    user = update.effective_user
    logger.info(f"Message from {user.id}: {text}")

    await update.message.reply_text("You said: " + text)
