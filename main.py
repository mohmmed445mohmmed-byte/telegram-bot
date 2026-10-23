import os
import sys
import logging
from telegram import Update
from telegram.ext import Application

os.environ["TELEGRAM_BOT_TOKEN"] = "8872859478:AAE5YDA9zKrZ6eyDOd2-l9PWidbRDjJAcUU"

def configure_logging() -> None:
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )
    logging.getLogger("httpx").setLevel(logging.WARNING)

def build_application(token: str) -> Application:
    return Application.builder().token(token).build()

def main() -> None:
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if not token:
        print("Missing TELEGRAM_BOT_TOKEN.", file=sys.stderr)
        raise SystemExit(1)

    configure_logging()
    application = build_application(token)
    logging.getLogger(__name__).info("Starting Telegram bot with long polling")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
  
