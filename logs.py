from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

def logs_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = open('logs.csv','a')
    file.write(f'{update.effective_user.first_name},{update.effective_user.id},{update.message.text}\n')
    file.close()