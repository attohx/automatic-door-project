from pprint import pprint
import requests
r = requests.get('https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}')
pprint(r.json)


import requests, json
api_key = "someapikey"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = ("Brunei")
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
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