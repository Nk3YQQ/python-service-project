from typing import Any

from src.services import make_title_list


class Parser:
    """
    Класс для парсинга полученных данных из таблицы Google Sheet
    """

    def __init__(self, data: list[list[Any]]) -> None:
        self._data = data

        self.headers = self._make_headers()
        self.body = data[1:]

    def _make_headers(self) -> list[str]:
        return make_title_list(self._data[0])

    def convert_data_to_dict(self) -> list[dict]:
        return list(dict(zip(self.headers, values)) for values in self.body)



