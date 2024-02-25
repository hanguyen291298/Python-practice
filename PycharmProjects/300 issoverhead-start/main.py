import time

import requests
from datetime import datetime
import smtplib

My_user = "han655442@gmail.com"
MY_password = "pyowqmqzprnsgnev"

MY_LAT = 14.473850 # Your latitude
MY_LONG = 108.186974 # Your longitude

current_iss = requests.get("http://api.open-notify.org/iss-now.json")
position = current_iss.json()
current_latitude = float(position["iss_position"]["latitude"])
current_longitude = float(position["iss_position"]["longitude"])


def iss_overhead():
    if MY_LAT - 5 <= current_latitude <= MY_LAT + 5 and MY_LONG - 5 <= current_longitude <= MY_LONG + 5:
        return True


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG
}

response = requests.get("https://api.sunrise-sunset.org/json?", params=parameters)
print(response.raise_for_status)
data = response.json()

sunset = data["results"]["sunset"].split(":")
sunrise = data["results"]["sunrise"].split(":")
print(sunrise)

# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



