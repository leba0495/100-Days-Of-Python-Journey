import requests
import html
from twilio.rest import Client
import config

# Stock
STOCK = "TSLA"
COMPANY_NAME = "Tesla, Inc."
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = config.stock_api_key
# News
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = config.news_api_key

# Twilio
TWILIO_SID = config.twilio_sid
TWILIO_AUTH_TOKEN = config.twilio_auth_token
TWILIO_PHONE = config.twilio_verified_number
RECIPIENT_PHONE = config.my_phone_number


def compare_prices(data_list):
    yesterday_price = float(data_list[0]["4. close"])
    day_before_price = float(data_list[1]["4. close"])
    percentage = round(((yesterday_price - day_before_price) / day_before_price) * 100)
    if percentage <= -5:
        return f"🔻{abs(percentage)}%"
    elif percentage >= 5:
        return f"🔺{percentage}%"


stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}
news_params = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
}

# Stock's data
stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stock_data.items()]

# News' data
news_response = requests.get(NEWS_ENDPOINT, params=news_params)
news_response.raise_for_status()
news_data = news_response.json()
articles_list = news_data["articles"][:3]

# List with each article's title
headlines = [article["title"] for article in articles_list]
# List with each article's description
descriptions = [article["description"] for article in articles_list]

price_change = compare_prices(stock_data_list)

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
# Loop to send an SMS with percentage change and each article's headlines, and brief descriptions.
for numb in range(len(articles_list)):
    message = client.messages.create(
        body=f"{STOCK}: {price_change} Headline: {html.unescape(headlines[numb])}.\n"
             f"Brief: {html.unescape(descriptions[numb])}.",
        from_=TWILIO_PHONE,
        to=RECIPIENT_PHONE
    )
    print(message.status)