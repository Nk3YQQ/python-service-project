from src.services import convert_clients_data, make_body, make_title_list


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
