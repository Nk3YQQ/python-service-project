import click

from src import settings
from src.google_api_auth import GoogleAPIAuth
from src.json_handler import JSONHandler
from src.parser import Parser
from src.validator import Validator


@click.command()
@click.option("--options_json", help="Уникальный номер продукта")
def main(options_json):
    """Функция для запуска приложения"""

    google_api_auth = GoogleAPIAuth()

    data = google_api_auth.get_sheets_data()

    parser = Parser(data)

    converted_client_data = parser.convert_clients_data()

    validator = Validator(converted_client_data)

    validator.write_result_to_json_file(settings.RESULT_PATH)

    json_handler = JSONHandler(converted_client_data, settings.DATAPATH)

    json_handler.write_data_to_file()

    data = json_handler.get_data_from_file(options_json)

    click.echo(data)


if __name__ == "__main__":
    main()
