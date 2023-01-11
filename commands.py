from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from logs import logs_command


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logs_command(update,context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name}!')