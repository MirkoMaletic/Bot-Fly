from telegram.ext import CommandHandler

async def start(update, context):
    await update.message.reply_text("Bot je aktivan i čeka komande.")

async def status(update, context):
    await update.message.reply_text("Status: Bot funkcioniše normalno.")

def register_handlers(app):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))