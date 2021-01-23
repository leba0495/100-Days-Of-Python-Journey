from twilio.rest import Client
from os import environ
import smtplib

TWILIO_SID = environ['TWILIO_SID']
TWILIO_AUTH_TOKEN = environ['TWILIO_AUTH_TOKEN']
VIRTUAL_TWILIO_NUMBER = environ["TWILIO_VERIFIED_PHONE"]
VERIFIED_NUMBER = environ["MY_NUMBER"]
EMAIL = environ["MY_EMAIL"]
EMAIL_PASS = environ["MY_PASSWORD"]


# noinspection PyMethodMayBeStatic
class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_low_price_alert(self, message):
        out_message = self.client.messages.create(
            body=message,
            from_=VIRTUAL_TWILIO_NUMBER,
            to=VERIFIED_NUMBER,
        )
        print(out_message.sid)

    def send_customer_email(self, message, user_email, flight_url):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=EMAIL_PASS)
            for user in user_email:
                connection.sendmail(
                    from_addr=EMAIL,
                    to_addrs=user,
                    msg=f"Subject:Lui's Flight Club Alert\n\n{message}\n{flight_url}"
                )
