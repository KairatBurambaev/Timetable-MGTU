from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from logs import logs_command
from timetable import main

async def timetable_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logs_command(update,context)
    response = main(update.message.text)
    await update.message.reply_text(response)