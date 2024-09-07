import threading
import time

from src import settings
from src.telegram_api_handler import TelegramAPIHandler


def start_bot():
    """Функция для запуска бота"""

    bot_token = settings.BOT_TOKEN
    bot_password = settings.BOT_PASSWORD
    telegram_handler = TelegramAPIHandler(bot_token, bot_password)

    bot_thread = threading.Thread(target=telegram_handler.get_updates)
    bot_thread.daemon = True
    bot_thread.start()

    while True:
        telegram_handler.send_notification_if_missing_fields(settings.RESULT_PATH)
        time.sleep(5)


if __name__ == "__main__":
    start_bot()
