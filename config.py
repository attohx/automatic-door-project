# =========================
# Poultry Gate Configuration
# =========================

# GPIO pin mappings (BCM mode)
PINS = {
    "SERVO": 18,          # Servo signal pin
    "LED_RED": 23,        # Red LED (closed)
    "LED_GREEN": 24,      # Green LED (open)
    "BUTTON": 17,         # Manual override button
    "LIMIT_OPEN": 25,     # Limit switch (door fully open)
    "LIMIT_CLOSED": 26,   # Limit switch (door fully closed)
    "I2C_SDA": 2,         # OLED SDA
    "I2C_SCL": 3          # OLED SCL
}

# Door schedule (24-hour format)
SCHEDULE = {
    "OPEN_HOUR": 6,       # Open door at 06:00
    "CLOSE_HOUR": 19      # Close door at 19:00
}

# Servo settings
SERVO = {
    "OPEN_DUTY": 7.5,     # Duty cycle for open position
    "CLOSE_DUTY": 2.5,    # Duty cycle for closed position
    "FREQ": 50            # Servo PWM frequency (Hz)
}

# Email alerts (if using SMTP)
EMAIL = {
    "MAIL_SERVER": "smtp.gmail.com",
    "MAIL_PORT": 587,
    "MAIL_USE_TLS": True,
    "MAIL_USE_SSL": False,
    "MAIL_USERNAME": "quayeadelaide18@gmail.com",
    "MAIL_PASSWORD": "gksv gvgh duiv ipbq",   # Gmail App Password
    "MAIL_DEFAULT_SENDER": "quayeadelaide18@gmail.com",
    "TO_EMAIL": "attohnathanan@gmail.com"
}

# Weather API
WEATHER = {
    "ENABLED": False,
    "API_KEY": "your_openweathermap_api_key",
    "CITY": "Accra",
    "UNITS": "metric"   # 'metric' for °C, 'imperial' for °F
}

# OLED display
OLED = {
    "ENABLED": True,
    "WIDTH": 128,
    "HEIGHT": 64
}

