from src.services import convert_data_to_json, open_json_file, write_json_file


class JSONHandler:
    """
    Класс для сохранения данных в формат json и их чтение
    """

    def __init__(self, data: list[dict], path):
        self._data = data
        self._path = path

    def write_data_to_file(self):
        """Запись данных в json файл"""

        write_json_file(self._path, self._data)

    def get_data_from_file(self, options_json: str) -> str:
        """Чтение данных из json-файла по полю 'options_json'"""

        data = open_json_file(self._path)

        filter_data = list(part for part in data if part["options_json"] == options_json)

        if not filter_data:
            return f"Данные по options_json '{options_json}' не найдены"

        return convert_data_to_json(filter_data)
