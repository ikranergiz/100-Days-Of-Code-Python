import requests
from datetime import datetime

USERNAME = "ikra"
TOKEN = ""
GRAPH_ID = ""

pixela_endpoint = "https://pixe.la/v1/users"


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# POST METHOD
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Reading Graph",
    "unit": "Page",
    "type": "int",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# POST METHOD with HEADERS
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
formatted_today = today.strftime("%Y%m%d")

pixel_data = {
    "date": formatted_today,
    "quantity": "10",
}

pixel_update_data = {
    "quantity": "25"
}

# POST METHOD
# response = requests.post(url=endpoint, json=pixel_data, headers=headers)
# print(response.text)

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_today}"

# PUT METHOD
# response = requests.put(url=pixel_update_endpoint, json=pixel_update_data, headers=headers)
# print(response.text)

pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_today}"

# DELETE METHOD
# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response.text)
