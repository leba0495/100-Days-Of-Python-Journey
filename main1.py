from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

ORIGIN_CITY_CODE = "NYC"
# Step 3
data_manager = DataManager()
sheet_data = data_manager.get_data_destination()
customer_data = data_manager.get_customer_emails()
flight_search = FlightSearch()
notificator = NotificationManager()

# If the city in the spreadsheet doesn't have a IATA Code this part will get it and update the spreadsheet
for row in range(len(sheet_data)):
    if sheet_data[row]['IATA Code'] == '':
        sheet_data[row]['IATA Code'] = flight_search.get_city_code(sheet_data[row]['City'])
        data_manager.data_destination = sheet_data
        data_manager.update_destination_code()

# Obtain dates
tomorrow = datetime.now() + timedelta(days=1)
six_months_from_now = tomorrow + timedelta(days=(6 * 30))

found_flights = True
for destination in sheet_data:
    flight = flight_search.search_for_flight(
        ORIGIN_CITY_CODE,
        destination['IATA Code'],
        from_date=tomorrow,
        to_date=six_months_from_now,
    )
    if flight is None:
        continue

    if flight.price < destination['Lowest Price']:
        message = f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to "\
                f"{flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to " \
                f"{flight.return_date}."
        if flight.stop_overs > 0:
            message += f"\nThis flight has {flight.stop_overs} stop over, via {flight.via_city} city."

        link = flight.flight_link
        # SMS
        notificator.send_low_price_alert(message)
        # Emails
        notificator.send_customer_email(message, customer_data, link)