from datetime import datetime
from geopy.geocoders import Nominatim
from timezonefinderL import TimezoneFinder
import pytz

def get_timezone_from_location(location_name):
    geolocator = Nominatim(user_agent="time_app")
    location = geolocator.geocode(location_name)

    if not location:
        print("DEBUG: Location not found.")
        return None, None

    print("DEBUG: Location object:", location)
    print("DEBUG: Latitude:", location.latitude, "Longitude:", location.longitude)

    tf = TimezoneFinder()
    timezone = tf.timezone_at(lng=location.longitude, lat=location.latitude)

    print("DEBUG: Timezone from timezonefinderL:", timezone)

    return timezone, location.address

def get_local_time(timezone):
    try:
        tz = pytz.timezone(timezone)
        now = datetime.now(tz)
        return now.strftime("%A, %Y-%m-%d %I:%M:%S %p")
    except Exception as e:
        print("DEBUG: Error in get_local_time:", e)
        return None

if __name__ == "__main__":
    location_name = input("Enter your city or country: ").strip()
    
    timezone, full_address = get_timezone_from_location(location_name)
    
    if timezone:
        local_time = get_local_time(timezone)
        print(f"📍 Location: {full_address}")
        print(f"🌍 Timezone: {timezone}")
        print(f"⏰ Local Time: {local_time}")
    else:
        print("❌ Could not determine timezone from that location.")

