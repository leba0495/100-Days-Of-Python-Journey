import requests
from os import environ
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = environ["TEQUILA_API_KEY"]


# noinspection PyMethodMayBeStatic
class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def get_city_code(self, city_name):
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", headers=headers, params=query)
        result = response.json()["locations"]
        code = result[0]['code']
        return code

    def search_for_flight(self, origin_city_code, destination_city_code, from_date, to_date):
        """The default flight is to get a direct flight, however if none is found the Tequila API will provide an
        empty request. The exception will request changing the stops to 2 in order to obtain a request with information.
        """
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_date.strftime("%d/%m/%Y"),
            "date_to": to_date.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 0,
            "max_stopovers": 0,
            "cur": "USD",
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", headers=headers, params=query)
        try:
            data = response.json()['data'][0]
        except IndexError:
            query["max_stopovers"] = 2
            result = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", headers=headers, params=query)
            data = result.json()['data'][0]
            flight_data = FlightData(
                price=data['price'],
                origin_city=data['route'][0]['cityFrom'],
                origin_airport=data['route'][0]['flyFrom'],
                destination_city=data['route'][1]['cityTo'],
                destination_airport=data['route'][1]['flyTo'],
                out_date=data['route'][0]['local_departure'].split('T')[0],
                return_date=data['route'][1]['local_departure'].split('T')[0],
                stop_overs=1,
                via_city=data['route'][0]['cityTo'],
                flight_link=data['deep_link']
            )
            return flight_data

        else:
            flight_data = FlightData(
                price=data['price'],
                origin_city=data['route'][0]['cityFrom'],
                origin_airport=data['route'][0]['flyFrom'],
                destination_city=data['route'][0]['cityTo'],
                destination_airport=data['route'][0]['flyTo'],
                out_date=data['route'][0]['local_departure'].split('T')[0],
                return_date=data['route'][1]['local_departure'].split('T')[0],
                flight_link=data['deep_link']
            )
            return flight_data
