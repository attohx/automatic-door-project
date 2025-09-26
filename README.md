# automatic-door-project

Project: Automatic Door Based on Time + Weather
#### ✅ What It Does

Opens the door at a scheduled time (e.g., 7:00 AM).

Closes it at sunset or a specific time (e.g., 7:00 PM).

Overrides schedule based on weather, like:

If raining → keep door closed

If wind is too strong → delay opening

If temperature is too low/high → auto-close for safety

## Required Hardware (Basic Version)
Component	Purpose	Notes
Raspberry Pi	Main controller	Any model with GPIO will do (Pi Zero W, 3B+, 4)
Servo Motor / Linear Actuator	Moves the door	Servo for light door, actuator for heavier ones
Motor Driver Board	Controls the motor safely	L298N or similar (for actuators)
Power Supply	Drives the motor (separate from Pi)	E.g., 12V for actuator, or 5V for servo
Limit Switches (x2)	Detect open/closed position	Prevents overdriving the motor
DHT22 or BME280 Sensor	Reads temp/humidity	For weather logic
Rain Sensor (YL-83 or similar)	Detects rainfall	Optional but useful
Real-Time Clock (RTC)	Keeps time if Pi restarts	Optional
(Optional) Wi-Fi	To fetch weather API data	If not using physical sensors
🧠 Software Logic (Simple Version)

At sunrise/time (7:00 AM):

If no rain and temp is safe, open the door.

At sunset/time (7:00 PM):

Close the door.

At any time:

If it starts raining, close the door.

If temp drops below X or wind > Y → auto-close.

### Option 1: Use Physical Sensors

Pros:

Works offline

No reliance on internet

Components:

DHT22/BME280 for temp/humidity

YL-83 for rain

Limit switches to detect door state

☁️ Option 2: Use Online Weather API

Pros:

More accurate (wind, UV, forecast)

Easy to expand logic

How:

Use Python + requests to fetch weather data from:

OpenWeatherMap

WeatherAPI

Tomorrow.io

Example JSON response:

{
  "temp": 17,
  "humidity": 80,
  "rain": true,
  "wind_speed": 24
}

## Motor Control Options
Type	Best For	Control Method
Servo Motor	Small/light doors	PWM via GPIO or board
Stepper Motor	Precise control (slower)	Stepper driver board
Linear Actuator	Heavy-duty outdoor doors	L298N + relays

You MUST use a separate power supply for motors — the Pi can't power them directly.

### Safety Features to Consider

Limit Switches: Stops the motor when fully opened/closed.

Manual Override Switch/Button

LED Indicators: Show current door state.

Error Log: If weather or sensor data fails.

## Example Build Scenario

You’re building a chicken coop door:

Opens at 6:30 AM

Closes at 7:30 PM

If raining or under 5°C, door stays closed

Uses:

Servo motor to lift sliding door

Rain sensor for local detection

DHT22 for temperature

Two limit switches to stop motor

## Software Tools & Libraries
Tool / Library	Use Case
Python	Main logic script
gpiozero	Control GPIOs easily
schedule	For time-based events (Python lib)
requests	For weather API calls
RPi.GPIO	For motor control
time & datetime	For timing logic
🧠 Bonus Features (If You Want to Expand Later)

Add a camera to capture motion or log door events

Connect to Home Assistant for remote monitoring

Display door state + weather on a small OLED screen

Send notifications via Telegram, email, or SMS

### ✅ Summary — The Basic Version
Feature	Solution
Scheduled opening/closing	Use schedule or cron in Python
Weather-based override	Rain + temp sensors or weather API
Motor control	Servo or linear actuator + GPIO
Safety	Limit switches to prevent overrun
