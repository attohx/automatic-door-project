from dotenv import load_dotenv
import os
import requests, json

load_dotenv()

api_key = os.getenv("WEATHER_API_KEY")
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = "Accra, Ghana"
complete_url = base_url + "q=" + city_name + "&appid=" + api_key
response = requests.get(complete_url)
x = response.json()
if x["cod"] != "404":
    y = x["main"]
    current_temperature = y["temp"]
    weathervar = x["weather"]
else:
    print(" City Not Found ")

if 'Rain' in weathervar:
    print("You don't need to water your plants today.")
else:
    print("You need to water your plants today")
    print(weathervar)