import os
from telegram.ext import ApplicationBuilder
from handlers.commands import register_handlers

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")

if not TELEGRAM_TOKEN:
    raise ValueError("TELEGRAM_TOKEN is not set in environment variables.")

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
register_handlers(app)
app.run_polling()