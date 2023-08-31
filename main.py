import requests
from twilio.rest import Client
from data import weather_api_key, account_sid, auth_token, sender, receiver

parameters = {
    "lat": 28.037960,
    "lon": -82.664270,
    "exclude": "current,minutely,daily",
    "appid": weather_api_key
}

response = requests.get(url="https://api.openweathermap.org/data/3.0/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()

times = weather_data["hourly"][:12]

for data in times:
    identification_code = data["weather"][0]['id']
    if identification_code < 700:
        print(f"bring an umbrella. Id: {identification_code}")
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body="It's going to rain today. Remember to bring an umbrella ☔ if you will go out.",
            from_=sender,
            to=receiver
        )
        print(message.status)
        break
