import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")

RANGE_NAME = os.getenv("RANGE_NAME")

BOT_TOKEN = os.getenv("BOT_TOKEN")

BOT_PASSWORD = os.getenv("BOT_PASSWORD")

CREDENTIALS_PATH = Path(__file__).parent.parent.joinpath("credentials.json")

DATAPATH = Path(__file__).parent.parent.joinpath("data", "data.json")

RESULT_PATH = Path(__file__).parent.parent.joinpath("data", "result.json")
