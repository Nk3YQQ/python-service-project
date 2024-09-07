import json
from typing import Any


def make_title_list(title_list: list[str]) -> list[str]:
    """Cоздание названия для заголовка"""

    return list(title.lower().strip().replace(" ", "_") for title in title_list if title)


def process_activity_time(activity_time: str) -> list[list[int]]:
    """Преобразование поля 'activity_time'"""

    numbers = list(map(int, activity_time.strip().split(",")))
    return list(numbers[i : i + 2] for i in range(0, len(numbers), 2))


def convert_element(element: str):
    """Конвертация элемента тела"""

    if element.isdigit():
        return int(element)

    strip_element = element.strip()

    if strip_element in ["true", "false"]:
        return bool(strip_element)

    split_element = element.split(",")

    if element == "0,1,2,3,4,5,6":
        return list(int(e) for e in split_element)

    if len(split_element) == 4 and all(part.strip().isdigit for part in split_element):
        return process_activity_time(element)

    return element


def check_on_empty_of_last_field(data: list[Any]) -> list[Any]:
    """Проверка последнего элемента тела на пустоту"""

    if not isinstance(data[-1], bool):
        data.append(False)

    return data


def make_body(data: list[list[str]]) -> list[Any]:
    """Создание тела данных"""

    return list(list(convert_element(list_data) for list_data in sublist) for sublist in data)


def convert_clients_data(body: list[list[Any]], headers: list[str]) -> list[dict]:
    """Конвертация данных клиента"""

    clients_data = []

    for data in body:
        del data[22]

        checked_data = check_on_empty_of_last_field(data)

        first_element = data[0]

        if first_element != "":
            client_data = {headers[0]: first_element}

        else:
            client_data = {headers[0]: clients_data[-1][headers[0]]}

        other_data = dict(zip(headers[1:], checked_data[1:]))

        merged_dict = client_data | other_data

        clients_data.append(merged_dict)

    return clients_data


def open_json_file(path):
    """Открытие файла в формате json"""
    try:
        with open(path, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


def write_json_file(path, data: list[dict] | dict):
    """Запись данных в json-фйал"""
    try:
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    except FileNotFoundError:
        raise FileNotFoundError("Файл по заданному пути не найден")


def convert_data_to_json(data: list[dict]) -> str:
    """Конвертация данных в json"""

    return json.dumps(data, indent=4, ensure_ascii=False)


def clear_data(path):
    """Заменяет исходные данные json-файла на {}"""
    try:
        with open(path, "w", encoding="utf-8") as file:
            file.write("{}")

    except FileNotFoundError:
        raise FileNotFoundError("Файл по заданному пути не найден")
