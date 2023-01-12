from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
from commands import timetable_request
from telegram.ext.filters import TEXT

app = ApplicationBuilder().token("5987250816:AAF29pfJMQ_9wp78JlLYM9813V4uio8NCis").build()

app.add_handler(MessageHandler(TEXT, timetable_request))

app.run_polling()