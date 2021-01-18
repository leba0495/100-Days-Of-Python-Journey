import requests
from datetime import datetime
import os

USERNAME = os.environ["USERNAME"]
TOKEN = os.environ["TOKEN"]
GRAPH_ID = "graph1"

# To create an account/user
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)

# Creating a graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Jogging Graph",
    "unit": "Mi",
    "type": "float",
    "color": "momiji",
}
headers = {
    "X-USER-TOKEN": TOKEN,
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Creating a pixel in the graph
pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many miles did you run today? "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

# Updating a pixel
pixel_update_endpoint = f"{pixel_creation_endpoint}/{pixel_data['date']}"

new_pixel_data = {
    "quantity": "3"
}
# response = requests.put(url=pixel_update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

# Deleting a pixel
delete_pixel = f"{pixel_update_endpoint}"
# response = requests.delete(url=delete_pixel, headers=headers)
# print(response.text)