from src.services import write_json_file


class Validator:
    """
    Класс для валидации пропусков при получении данных пользователем
    """

    def __init__(self, data: list[dict]):
        self._data = data

    def _check_data_for_empty(self):
        """Проверяет значения данных на пустоту"""

        return any(value == "" for item in self._data for value in item.values())

    def write_result_to_json_file(self, path):
        result = self._check_data_for_empty()

        data = {"result": result}

        write_json_file(path, data)
