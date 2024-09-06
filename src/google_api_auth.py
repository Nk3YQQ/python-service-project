from typing import Any

from google.oauth2 import service_account
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

from src import settings
from src.settings import CREDENTIALS_PATH


class GoogleAPIAuth:
    """
    Класс для работы с авторизацией и получением данных из таблицы Google Sheets
    """

    def __init__(self) -> None:
        self._scopes: list[str] = settings.SCOPES
        self._spreadsheet_id: str = settings.SPREADSHEET_ID
        self._range_name: str = settings.RANGE_NAME

        self._credentials: Credentials = self._get_credentials()
        self._spreadsheet_service = self._get_spreadsheet_service()
        self._sheet = self._get_sheet()

    def _get_credentials(self) -> Credentials:
        """
        Получение учётных данных из JSON-файла для сервисного аккаунта
        """
        try:
            return service_account.Credentials.from_service_account_file(CREDENTIALS_PATH, scopes=self._scopes)

        except Exception as e:
            raise ValueError(f"Ошибка при получении учётных данных: {e}")

    def _get_spreadsheet_service(self):
        """
        Инициализация сервиса Google Sheets API
        """
        return build("sheets", "v4", credentials=self._credentials)

    def _get_sheet(self):
        """
        Возвращение объекта для работы с листами таблицы
        """
        return self._spreadsheet_service.spreadsheets()

    def get_sheets_data(self) -> list[list[Any]]:
        """
        Получение данных из указанного диапазона таблицы
        """
        try:
            result = self._sheet.values().get(spreadsheetId=self._spreadsheet_id, range=self._range_name).execute()
            return result.get("values", [])

        except Exception as e:
            raise ValueError(f"Ошибка при получении данных из Google Sheet таблицы: {e}")
