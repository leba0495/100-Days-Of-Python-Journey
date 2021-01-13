import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 41.67864791350729  # Your latitude
MY_LONG = -72.86885179720166  # Your longitude
MY_EMAIL = "your email"
MY_PASSWORD = "you password"


# Your position is within +5 or -5 degrees of the ISS position.
def confirm_position():
    # Get ISS information
    pos_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    pos_response.raise_for_status()
    iss_data = pos_response.json()
    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])
    if (int(MY_LAT) - 5) <= iss_latitude <= (int(MY_LAT) + 5) and \
            (int(MY_LONG) - 5) <= iss_longitude <= (int(MY_LONG) + 5):
        return True
    else:
        return False


def confirm_nighttime():
    # Get current day information
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    time_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    time_response.raise_for_status()
    time_data = time_response.json()
    sunrise = int(time_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(time_data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True
    else:
        return False


# If the ISS is close to my current position  and it is currently dark
while True:
    time.sleep(60)
    if confirm_position() and confirm_nighttime():
        # Then send me an email to tell me to look up.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="ab.luis04@gmail.com",
                msg="Subject:ISS Notification\n\nLook up! the ISS is above you."
            )
