import requests
from datetime import datetime

MY_LAT = 40.728226
MY_LNG = -73.794853
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()
# longitude = data["iss_position"]['longitude']
# latitude = data["iss_position"]['latitude']
# iss_pos = (longitude, latitude)
# print(iss_pos)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

timenow = datetime.now()

print(sunrise)
print(sunset)