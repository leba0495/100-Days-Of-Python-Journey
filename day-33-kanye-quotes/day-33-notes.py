import requests
from datetime import datetime
MY_LAT = 40.6501038
MY_LNG = -73.9495823
HOUR_FORMAT = 0

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": HOUR_FORMAT,
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data)
# Use the split method to isolate the hour from the sunrise data
sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]
sunset = data['results']['sunset'].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)
time_now = datetime.now()

print(time_now.hour)