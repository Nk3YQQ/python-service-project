import click

from src.google_api_auth import GoogleAPIAuth
from src.json_handler import JSONHandler
from src.parser import Parser
from src.settings import DATAPATH


@click.command()
@click.option("--options_json", help="Уникальный номер продукта")
def main(options_json):
    google_api_auth = GoogleAPIAuth()

    data = google_api_auth.get_sheets_data()

    parser = Parser(data)

    converted_client_data = parser.convert_clients_data()

    json_handler = JSONHandler(converted_client_data, DATAPATH)

    json_handler.write_data_to_file()

    data = json_handler.get_data_from_file(options_json)

    click.echo(data)


if __name__ == "__main__":
    main()
