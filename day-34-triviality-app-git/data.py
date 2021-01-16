import requests

# Everytime the code is compiled there will be a new set of questions

NUMB_OF_QUESTION = 10
TYPE_OF_QUESTIONS = "boolean"

parameters = {
    "amount": NUMB_OF_QUESTION,
    "type": TYPE_OF_QUESTIONS,
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()

question_data = data["results"]
