import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# =========================
# Poultry Gate Configuration
# =========================

PINS = {
    "SERVO_PIN": 11,
    "LED_RED": 12,
    "LED_GREEN": 24,
    "BUTTON": 17,
    "LIMIT_OPEN": 25,
    "LIMIT_CLOSED": 26,
    "I2C_SDA": 2,
    "I2C_SCL": 3
}

SCHEDULE = {
    "OPEN_HOUR": 6,
    "CLOSE_HOUR": 19
}

SERVO = {
    "OPEN_DUTY": 7.5,
    "CLOSE_DUTY": 2.5,
    "FREQ": 50
}

TO_EMAIL = "attohnathanan@gmail.com"

EMAIL = {
    "MAIL_SERVER": os.getenv("MAIL_SERVER"),
    "MAIL_PORT": int(os.getenv("MAIL_PORT", 587)),
    "MAIL_USE_TLS": os.getenv("MAIL_USE_TLS", "True") == "True",
    "MAIL_USE_SSL": os.getenv("MAIL_USE_SSL", "False") == "True",
    "MAIL_USERNAME": os.getenv("MAIL_USERNAME"),
    "MAIL_PASSWORD": os.getenv("MAIL_PASSWORD"),
    "MAIL_DEFAULT_SENDER": os.getenv("MAIL_DEFAULT_SENDER"),
}

WEATHER = {
    "ENABLED": True,
    "API_KEY": os.getenv("WEATHER_API_KEY"),
    "CITY": os.getenv("WEATHER_CITY", "Accra"),
    "UNITS": os.getenv("WEATHER_UNITS", "metric")
}

OLED = {
    "ENABLED": True,
    "WIDTH": 128,
    "HEIGHT": 64
}

# =========================
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password123"   # later we can hash this for extra security
SECRET_KEY = "super_secret_key"  # for Flask sessions
