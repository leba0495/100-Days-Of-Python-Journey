import requests
from datetime import datetime
import os

APP_ID = os.getenv("APP_ID")
APP_KEY = os.getenv("APP_KEY")
SHEETY_USER = os.getenv("SHEETY_USER")
SHEETY_PASS = os.getenv("SHEETY_PASS")

GENDER = os.getenv("GENDER")
WEIGHT_KG = os.getenv("WEIGHT_KG")
HEIGHT_CM = os.getenv("HEIGHT_CM")
AGE = os.getenv("AGE")

nutrionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = os.getenv("SHEETY_ENDPOINT")

exercise_by_user = input("Tell me which exercises you did:\n")

nutritionix_params = {
    "query": exercise_by_user,
    "gender": "male",
    "weight_kg": 79.37,
    "height_cm": 173.73,
    "age": 25
}
headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "x-remote-user-id": "0",
}

response = requests.post(
    url=nutrionix_endpoint, json=nutritionix_params, headers=headers)
response.raise_for_status()
result = response.json()['exercises']

today = datetime.now()
today_date = today.strftime("%x")
today_time = today.strftime("%X")

for exercise in result:
    sheety_params = {
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories'],
        }
    }
    sheety_response = requests.post(
        url=sheety_endpoint,
        json=sheety_params,
        auth=(SHEETY_USER, SHEETY_PASS))
    sheety_response.raise_for_status()
    print(sheety_response.json())
