import os

import requests
from twilio.rest import Client

OWM_Endpoints = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("OWM_API_KEY")

account_sid = "AC6f27416fa93c67b62a8f3948834e83a6"
auth_token = os.environ.get("AUTH_TOKEN")

MY_LAT = 40.912420  # 41.008240
MY_LONG = 40.149180  # 28.978359

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoints, params=weather_params)
response.raise_for_status()
weather_data = response.json()

weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]

    if int(condition_code) > 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella",
        from_="+18638692878",
        to=os.environ.get("PHONE_NUMBER")
    )
    print(message.status)
