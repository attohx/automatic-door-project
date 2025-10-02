import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather(city="Accra"):
    """
    Fetch weather data for the given city.
    Default city is Accra if none is provided.
    """
    try:
        if not API_KEY:
            return {"error": "API key not found. Please set OPENWEATHER_API_KEY in .env"}

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)

        if response.status_code != 200:
            return {"error": f"Failed to fetch weather for {city}"}

        data = response.json()

        # Extract relevant fields
        weather_info = {
            "city": data.get("name", city),
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"].capitalize(),
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }

        return weather_info

    except Exception as e:
        return {"error": str(e)}
