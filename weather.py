import requests
import config

def get_weather():
    if not config.WEATHER["ENABLED"]:
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
            return {
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "condition": data["weather"][0]["description"],
                "city": config.WEATHER["CITY"]
            }
        else:
            return {"error": f"API Error: {data.get('message', 'Unknown error')}"}
    except Exception as e:
        return {"error": f"Request failed: {e}"}
