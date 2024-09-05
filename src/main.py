from src.google_api_auth import GoogleAPIAuth
from src.parser import Parser


def main():
    google_api_auth = GoogleAPIAuth()

    data = google_api_auth.get_sheets_data()

    parser = Parser(data)

    print(parser.convert_data_to_dict())


if __name__ == '__main__':
    main()
