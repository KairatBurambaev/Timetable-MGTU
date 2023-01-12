from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
from commands import timetable_request
from telegram.ext.filters import TEXT

with open('.env','r') as file:
    token = file.readline()
app = ApplicationBuilder().token(token).build()

app.add_handler(MessageHandler(TEXT, timetable_request))

app.run_polling()