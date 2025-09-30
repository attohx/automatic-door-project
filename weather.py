import requests
import config

def get_weather():
    if not config.WEATHER["ENABLED"]:
        print("Weather system disabled in config.")
        return None

    url = (
        f"http://api.openweathermap.org/data/2.5/weather?"
        f"q={config.WEATHER['CITY']}"
        f"&appid={config.WEATHER['API_KEY']}"
        f"&units={config.WEATHER['UNITS']}"
    )

    try:
        response = requests.get(url, timeout=5)
        data = response.json()

        if response.status_code == 200:
            weather = {
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "condition": data["weather"][0]["description"],
                "id": data["weather"][0]["id"]  
            }
            return weather
        else:
            print(f"Weather API error: {data}")
            return None
    except Exception as e:
        print(f"Weather API request failed: {e}")
        return None

