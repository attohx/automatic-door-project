from datetime import datetime
import zoneinfo  # Built-in from Python 3.9+

def get_local_time(timezone):
    """Get current time in the given timezone."""
    try:
        tz = zoneinfo.ZoneInfo(timezone)
        now = datetime.now(tz)
        return now.strftime("%A, %Y-%m-%d %I:%M:%S %p")
    except Exception:
        return None

if __name__ == "__main__":
    print("Enter your timezone (example: Africa/Accra, Europe/London, America/New_York)")
    timezone = input("Timezone: ").strip()

    local_time = get_local_time(timezone)

    if local_time:
        print(f" Local Time in {timezone}: {local_time}")
    else:
        print(" Invalid timezone. Please try again.")
