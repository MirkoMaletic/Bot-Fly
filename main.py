from handlers.commands import setup_handlers
from telegram.ext import Application
import os

async def main():
    app = Application.builder().token(os.getenv("TELEGRAM_TOKEN")).build()
    setup_handlers(app)
    await app.start()
    await app.updater.start_polling()
    await app.updater.idle()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
