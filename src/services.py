from typing import Any


def make_title_list(title_list: list[str]) -> list[str]:
    return list(title.lower().strip().replace(' ', '_') for title in title_list if title)


def convert_data_to_dict(headers: list[str], values: list[Any]) -> dict:
    return dict(zip(headers, values))
