import requests
from twilio.rest import Client

account_sid = "ACc3f9aa622bc575ea199d31f842d8aa8f"
auth_token = "a0e2393db4a821a8bbfb54d315dd2516"


prameters = {
    "lat": 13.769040,
    "lon": 109.228371,
    "appid": "70f46b4499653205fae1584e6240646c"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/weather?", params=prameters)
response.raise_for_status()
data = response.json()

will_rain = False

if data["weather"][0]["id"] > 700:
    will_rain = True
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="it's not seems raining now",
        from_="+17073772083",
        to="+84394836655"
    )

    print(message.status)

