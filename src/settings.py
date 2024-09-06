import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")

RANGE_NAME = os.getenv("RANGE_NAME")

CREDENTIALS_PATH = Path(__file__).parent.parent.joinpath("credentials.json")

DATAPATH = Path(__file__).parent.parent.joinpath("data", "data.json")
