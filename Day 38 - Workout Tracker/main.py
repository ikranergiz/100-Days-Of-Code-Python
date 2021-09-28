import os
import requests
from datetime import datetime


APP_ID = os.environ['NT_APP_ID']
API_KEY = os.environ['NT_API_KEY']

USERNAME = os.environ['SHEETY_USERNAME']
PASSWORD = os.environ['SHEETY_PASSWORD']


GENDER = "female"
AGE = 20
WEIGHT = 54
HEIGHT = 170

nutritionix_endpoint = "https://trackapi.nutritionix.com"
nutritionix_exercises_endpoint = f"{nutritionix_endpoint}/v2/natural/exercise"
sheety_endpoint = os.environ['SHEETY_ENDPOINT']

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
    "Authorization": "Basic"
}

exercises_data = {
    "query": "exercise",
    "gender": GENDER,
    "age": AGE,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT
}

response = requests.post(url=nutritionix_exercises_endpoint, headers=headers, json=exercises_data)
data = response.json()


user_input = input("Tell me which exercises you did: ")
user_input_words = user_input.split()
exercise = user_input_words[0]

duration_min = float(data["exercises"][0]["duration_min"])
calories = float(data["exercises"][0]["nf_calories"])

today = datetime.now()

formatted_today = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")

sheety_data = {
    "workout": {
        "date": formatted_today,
        "time": time,
        "exercise": exercise,
        "duration": duration_min,
        "calories": calories
    }
}

# POST METHOD NO AUTHENTICATION
# response = requests.post(url=sheety_endpoint, json=sheety_data, headers=headers)
# print(response.text)

# POST METHOD WITH AUTHENTICATION
response = requests.post(url=sheety_endpoint, json=sheety_data, headers=headers, auth=(USERNAME, PASSWORD))
print(response.text)
