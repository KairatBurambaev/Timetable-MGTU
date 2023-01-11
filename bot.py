from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from commands import hi_command

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

app = ApplicationBuilder().token("5987250816:AAF29pfJMQ_9wp78JlLYM9813V4uio8NCis").build()

app.add_handler(CommandHandler("Hi", hi_command))

app.run_polling()