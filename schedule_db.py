import json
import os

SCHEDULE_FILE = "schedule.json"

# Default weekly schedule (all "Not set" initially)
DEFAULT_SCHEDULE = {
    "Monday": {"open_time": "Not set", "close_time": "Not set"},
    "Tuesday": {"open_time": "Not set", "close_time": "Not set"},
    "Wednesday": {"open_time": "Not set", "close_time": "Not set"},
    "Thursday": {"open_time": "Not set", "close_time": "Not set"},
    "Friday": {"open_time": "Not set", "close_time": "Not set"},
    "Saturday": {"open_time": "Not set", "close_time": "Not set"},
    "Sunday": {"open_time": "Not set", "close_time": "Not set"},
}


def _load_data():
    """Helper to load JSON or return default schedule."""
    if not os.path.exists(SCHEDULE_FILE):
        return DEFAULT_SCHEDULE.copy()
    try:
        with open(SCHEDULE_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return DEFAULT_SCHEDULE.copy()


def _save_data(data):
    """Helper to save JSON file."""
    with open(SCHEDULE_FILE, "w") as f:
        json.dump(data, f, indent=4)


def get_schedule():
    """Return the full weekly schedule."""
    return _load_data()


def get_day_schedule(day):
    """Return the schedule for a specific day."""
    data = _load_data()
    return data.get(day, {"open_time": "Not set", "close_time": "Not set"})


def update_schedule(day, open_time, close_time):
    """Update schedule for a specific day."""
    data = _load_data()
    data[day] = {"open_time": open_time, "close_time": close_time}
    _save_data(data)
    print(f"✅ Schedule updated for {day}: {open_time} - {close_time}")
