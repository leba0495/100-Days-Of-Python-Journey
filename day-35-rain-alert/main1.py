import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

# Info for request from OpenWeather
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall?"
API_KEY = os.environ.get("OMW_API_KEY")
MY_LAT = 40.678177
MY_LONG = -73.944160

# Info for twilio functionality
account_sid = "AC1e6a6f8e68b0b3b68d7cb65aa5371f20"
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily,alert"

}


def check_for_rain(code_list):
    for code in code_list:
        if code < 700:
            return True
    return False


response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
hourly_data_list = weather_data["hourly"][0:12]


weather_codes = [hour["weather"][0]["id"] for hour in hourly_data_list]

if check_for_rain(weather_codes):

    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella ☂️",
        from_="+19495580047",
        to="+16464705796"
    )
    print(message.status)
