import gspread
from oauth2client.service_account import ServiceAccountCredentials

SHEET_ID = "Copy of FLight Deals"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
                      "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name("FlightDeals.json", self.scope)
        self.client = gspread.authorize(self.credentials)
        self.sheet_instance = self.client.open("Copy of Flight Deals").worksheets()
        self.data_destination = {}

    def get_data_destination(self):
        self.data_destination = self.sheet_instance[0].get_all_records()
        return self.data_destination

    def update_destination_code(self):
        row = 2
        col = 2
        for city in range(len(self.data_destination)):
            self.sheet_instance[0].update_cell(row, col, self.data_destination[city]["IATA Code"])
            row += 1

    def get_customer_emails(self):
        customer_data = self.sheet_instance[1].get_all_records()
        emails = [row['Email'] for row in customer_data]
        return emails

    def add_new_user(self, name, last_name, email_address):
        row_information = [name, last_name, email_address]
        self.sheet_instance[1].insert_row(values=row_information, index=2)
