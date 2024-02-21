#api_key = "7bfe4894bea0b801653e7098e61d1326"
#api_key2 = "9d40a9a6f19083a1716b2fb168166540"

import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "7bfe4894bea0b801653e7098e61d1326"
account_sid = "AC18f4d2aab1b8db0bc4d054ea41d51124"
auth_token = "e26259ec1eb17a5cb945a15734b111b3"

weather_params = {
    "lat": 46.947975,
    "lon": 7.447447,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="+18556312587",
        to="YOUR TWILIO VERIFIED REAL NUMBER" # I am not putting my real number.
    )
    print(message.status)