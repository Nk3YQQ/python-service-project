import requests

from src.services import clear_data, open_json_file


class TelegramAPIHandler:
    """
    Класс для взаимодействия с API телеграмма
    """

    def __init__(self, token: str, password: str):
        self._token = token
        self._password = password

        self._authenticated_users = {}
        self._message_url = f"https://api.telegram.org/bot{self._token}/sendMessage"
        self._updates_url = f"https://api.telegram.org/bot{self._token}/getUpdates"

        self._offset = 0

    def _send_message(self, chat_id, text: str):
        """Отправка сообщения для пользователя"""

        requests.post(url=self._message_url, json={"chat_id": chat_id, "text": text})

    def _handle_message(self, message):
        """Обработка сообщений от пользователя"""

        chat_id = message["chat"]["id"]
        text: str = message.get("text", "")

        if chat_id not in self._authenticated_users:
            if text.lower() in ["/start", "старт"]:
                msg = "Введите пароль для аутентификации:"
                self._send_message(chat_id, msg)

            elif text == self._password:
                self._authenticated_users[chat_id] = True
                msg = "Аутентификация прошла успешно! Здесь вы будете получать уведомления об ошибках."
                self._send_message(chat_id, msg)

            elif text.lower() == "разлогиниться":
                del self._authenticated_users[chat_id]
                msg = "Вы разлогинились. Если снова хотите получать уведомления, отправьте 'Cтарт для аутентификации'"

            else:
                msg = "Неверный пароль. Попробуйте ещё раз"
                self._send_message(chat_id, msg)

        else:
            msg = "Вы уже аутентифицированы. Ожидайте уведомлений."
            self._send_message(chat_id, msg)

    def get_updates(self):
        """Получение новых сообщений от бота"""
        while True:
            response = requests.get(self._updates_url, params={"offset": self._offset})
            updates = response.json()

            for update in updates["result"]:
                self._handle_message(update["message"])
                self._offset = update["update_id"] + 1

    @staticmethod
    def _check_result_from_json_file(path):
        """Чтение результата их json файла"""

        data = open_json_file(path)

        if data:
            result = data["result"]

            clear_data(path)
        else:
            result = None

        return result

    def send_notification_if_missing_fields(self, path):
        """Отправление уведомлений в случае отсутствия какого-нибудь поля"""

        result = self._check_result_from_json_file(path)

        if result:
            for chat_id in self._authenticated_users:
                msg = "Проверьте поля на наличие пробелов! У некоторых клиентов отсутствуют обязательные поля"
                self._send_message(chat_id, msg)
