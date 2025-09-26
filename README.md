# 🐔 Automatic Poultry Gate using Raspberry Pi

An automated poultry door system that opens and closes based on time, weather, and/or light. Designed for small-scale or backyard farms to improve convenience, safety, and chicken welfare.

---

## ✅ Features

- Automatically **opens in the morning** and **closes in the evening**
- Manual **override button**
- **LED indicators** (green for open, red for closed)
- **OLED display** shows door status and weather info
- **Limit switches** prevent overdriving the motor
- Easily expandable with weather sensors or APIs

---

## 📦 Things We Need

| Component | Purpose |
|----------|---------|
| 🧠 **Raspberry Pi** (Zero W, 3B+, 4, etc.) | Main controller |
| ⚙️ **Servo Motor** | Opens/closes the door |
| 🔋 **Power Supply for Servo Motor** | Powers motor safely |
| 🔘 **Limit Switches (x2)** | Detect fully open/closed states |
| 🔴🟢 **LED Lights (x2)** | Status indicators (Red = closed, Green = open) |
| ⬛ **Push Button** | Manual override |
| 🖥️ **OLED LCD Display** (e.g. SSD1306) | Displays door status / weather |

---

## ⚙️ Basic Wiring Overview

| Component | GPIO Pin Example |
|-----------|------------------|
| Servo Signal | GPIO18 |
| Red LED | GPIO23 |
| Green LED | GPIO24 |
| Button | GPIO17 |
| Limit Switch 1 (Open) | GPIO25 |
| Limit Switch 2 (Closed) | GPIO26 |
| OLED Display (I2C) | SDA: GPIO2, SCL: GPIO3 |

> **Note:** Use resistors with LEDs and button (e.g. 220Ω for LEDs, 10kΩ pull-down for button)

---

## 🧰 Software Requirements

Install dependencies:

```bash
sudo apt update
sudo apt install python3-pip python3-gpiozero i2c-tools
pip3 install schedule adafruit-circuitpython-ssd1306 requests
Enable I2C (for OLED):

bash
Copy code
sudo raspi-config
# Go to: Interface Options > I2C > Enable
🧪 Basic Functionality
Script runs continuously and checks current time

At set times (e.g., 06:30 and 19:30), it triggers the servo to open/close the door

LED and display update accordingly

If button is pressed, toggles door state manually

Limit switches stop movement when door is fully open or closed


## 🚀 Getting Started
Clone the repo:

bash
Copy code
git clone https://github.com/your-username/auto-poultry-gate.git
cd auto-poultry-gate
Edit the schedule/times in gate_control.py

Run the script:

bash
Copy code
python3 gate_control.py
(Optional) Add to crontab or systemd for auto-start on boot

## 📸 Coming Soon
Wiring diagram

3D printable case / servo mount

Weather API integration (OpenWeatherMap)

## 🧠 Why This Matters
This project solves real problems in the farming world:

Protects chickens from predators by closing at night

Saves time and manual effort

Works even when farmer is away or unavailable

Expandable with weather data, camera, remote notifications, etc.
