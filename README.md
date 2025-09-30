
# 🐔 Automatic Poultry Gate (Raspberry Pi)

>An automated poultry door system for small-scale and backyard farms. Opens and closes the coop door based on time, weather, and/or light, improving convenience, safety, and chicken welfare.

---

## 🚀 Features

- **Automatic Scheduling:** Opens in the morning, closes in the evening
- **Manual Override:** Push button for manual control
- **LED Indicators:** Green (open), Red (closed)
- **OLED Display:** Shows door status and weather info
- **Limit Switches:** Prevents overdriving the motor
- **Weather Integration:** Expandable with sensors or APIs
- **Safety:** Protects chickens from predators

---

## �️ Hardware Required

| Component                                   | Purpose                                 |
|---------------------------------------------|-----------------------------------------|
| 🧠 Raspberry Pi (Zero W, 3B+, 4, etc.)      | Main controller                         |
| ⚙️ Servo Motor                              | Opens/closes the door                   |
| 🔋 Power Supply for Servo Motor             | Powers motor safely                     |
| 🔘 Limit Switches (x2)                      | Detect fully open/closed states         |
| 🔴🟢 LED Lights (x2)                         | Status indicators (Red = closed, Green = open) |
| ⬛ Push Button                              | Manual override                         |
| 🖥️ OLED LCD Display (e.g. SSD1306, I2C)     | Displays door status / weather          |
| 💧 Water Sensor (optional)                  | Environmental expansion                 |
| 🕵️ PIR Motion Sensor (optional)             | Detects movement near the coop          |

---

## 🪛 Wiring Overview

| Component              | GPIO Pin Example         |
|------------------------|-------------------------|
| Servo Signal           | GPIO18                  |
| Red LED                | GPIO23                  |
| Green LED              | GPIO24                  |
| Button                 | GPIO17                  |
| Limit Switch 1 (Open)  | GPIO25                  |
| Limit Switch 2 (Closed)| GPIO26                  |
| OLED Display (I2C)     | SDA: GPIO2, SCL: GPIO3  |

> **Note:** Use resistors with LEDs and button (e.g. 220Ω for LEDs, 10kΩ pull-down for button)

---

## 💡 Why Use This Project?

- **Protects chickens** from predators by closing at night
- **Saves time** and manual effort
- **Works unattended** (farmer can be away)
- **Expandable:** Add weather data, camera, remote notifications, and more

---

## 📂 Project Structure

- `app.py` — Main application logic
- `door.py` — Door control logic
- `limit_switch.py` — Limit switch handling
- `weather.py` — Weather API integration
- `mail.py` — Email notifications
- `config.py` — Configuration settings
- `templates/` — Web dashboard and weather display
- `practice/` — Test scripts and hardware experiments

---

## 📦 Installation & Setup

1. **Clone the repository:**
	```bash
	git clone <repo-url>
	cd poultry-system
	```
2. **Install dependencies:**
	```bash
	pip install -r requirements.txt
	```
3. **Configure your hardware:**
	- Connect components as per the wiring table above
	- Edit `config.py` for your setup
4. **Run the app:**
	```bash
	python app.py
	```

---

## 📖 Documentation

See `FEATURES.md` and `TASKS.md` for more details on features and development tasks.

---

## 📝 License

MIT License. See `LICENSE` file for details.
