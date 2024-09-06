from src.services import make_title_list, make_body, convert_clients_data


class Parser:
    """
    Класс для парсинга полученных данных из таблицы Google Sheet
    """

    def __init__(self, data: list[list[str]]) -> None:
        self._header = make_title_list(data[0])
        self._body = make_body(data[1:])

    def convert_clients_data(self) -> list[dict]:
        """
        Метод для конвертации данных клиента
        """
        return convert_clients_data(self._body, self._header)
