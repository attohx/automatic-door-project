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

## 🧠 Why This Matters
This project solves real problems in the farming world:

Protects chickens from predators by closing at night

Saves time and manual effort

Works even when farmer is away or unavailable

Expandable with weather data, camera, remote notifications, etc.
