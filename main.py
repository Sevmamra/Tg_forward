from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import logging
import asyncio
import os
from handlers import start_command, help_command, message_handler
from utils import load_env_variables

# Logging setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Load environment variables
load_env_variables()

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    logger.error("BOT_TOKEN not found in environment variables.")
    exit()

# Initialize application
app = Application.builder().token(TOKEN).build()

# Command Handlers
app.add_handler(CommandHandler("start", start_command))
app.add_handler(CommandHandler("help", help_command))

# Message Handlers
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

# Run bot
if __name__ == "__main__":
    logger.info("Bot is starting...")
    app.run_polling()
