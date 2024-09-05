import os

from dotenv import load_dotenv

load_dotenv()

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

SPREADSHEET_ID = os.getenv('SPREADSHEET_ID')

RANGE_NAME = os.getenv('RANGE_NAME')
