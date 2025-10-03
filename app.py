from flask import Flask, render_template, redirect, url_for, request, session, flash, jsonify
from config import EMAIL, TO_EMAIL, ADMIN_USERNAME, ADMIN_PASSWORD, SECRET_KEY
from mail import mail, send_email
from weather import get_weather
import state
import logs_db
import db_setup
import heat_lamp_state  # Heat lamp state manager
import schedule_db      # Weekly schedule manager
from datetime import datetime

app = Flask(__name__)
app.config.update(EMAIL)
app.secret_key = SECRET_KEY
mail.init_app(app)

# Initialize DB
dbstart = db_setup.kreatedb()

# -------------------- LOGIN SYSTEM --------------------

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session["username"] = username
            flash("Login successful!", "success")
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid credentials", "danger")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("username", None)
    flash("You have been logged out", "info")
    return redirect(url_for("login"))


# -------------------- MAIN DASHBOARD --------------------

@app.route("/")
def dashboard():
    if "username" not in session:
        flash("Please log in first", "warning")
        return redirect(url_for("login"))

    try:
        dbstart
    except:
        print("Error: Database could not be created")

    gate_status = state.get_state()
    lamp_status = heat_lamp_state.get_state()

    # Weather location from session
    city = session.get("weather_city", None)
    weather = get_weather(city)

    recent_logs = logs_db.read_logs(10)
    schedule = schedule_db.get_schedule()

    return render_template(
        "dashboard.html",
        gate_status=gate_status,
        lamp_status=lamp_status,
        weather=weather,
        logs=recent_logs,
        schedule=schedule
    )


# -------------------- WEATHER SETTINGS --------------------

@app.route("/set_city", methods=["POST"])
def set_city():
    if "username" not in session:
        flash("Please log in first", "warning")
        return redirect(url_for("login"))

    city = request.form.get("city")
    if not city:
        flash("City cannot be empty", "danger")
        return redirect(url_for("dashboard"))

    session["weather_city"] = city
    flash(f"Weather location updated to {city}", "success")
    return redirect(url_for("dashboard"))


# -------------------- GATE CONTROLS --------------------

@app.route("/open")
def open_gate():
    if "username" not in session:
        return redirect(url_for("login"))

    if state.get_state() == "OPEN":
        flash("Gate is already OPEN!", "info")
        return redirect(url_for("dashboard"))

    state.set_state("OPEN")
    logs_db.log_action("OPENED", session["username"])
    send_email("Poultry Gate Opened 🟢", "The poultry gate has been opened.", [TO_EMAIL])
    return redirect(url_for("dashboard"))


@app.route("/close")
def close_gate():
    if "username" not in session:
        return redirect(url_for("login"))

    if state.get_state() == "CLOSED":
        flash("Gate is already CLOSED!", "info")
        return redirect(url_for("dashboard"))

    state.set_state("CLOSED")
    logs_db.log_action("CLOSED", session["username"])
    send_email("Poultry Gate Closed 🔴", "The poultry gate has been closed.", [TO_EMAIL])
    return redirect(url_for("dashboard"))


# -------------------- HEAT LAMP CONTROLS --------------------

@app.route("/lamp/on")
def lamp_on():
    if "username" not in session:
        return redirect(url_for("login"))

    if heat_lamp_state.get_state() == "ON":
        flash("Heat Lamp is already ON!", "info")
        return redirect(url_for("dashboard"))

    heat_lamp_state.set_state("ON")
    logs_db.log_action("HEAT LAMP ON", session["username"])
    send_email("Heat Lamp Turned ON 🔥", "The heat lamp has been switched ON.", [TO_EMAIL])
    return redirect(url_for("dashboard"))


@app.route("/lamp/off")
def lamp_off():
    if "username" not in session:
        return redirect(url_for("login"))

    if heat_lamp_state.get_state() == "OFF":
        flash("Heat Lamp is already OFF!", "info")
        return redirect(url_for("dashboard"))

    heat_lamp_state.set_state("OFF")
    logs_db.log_action("HEAT LAMP OFF", session["username"])
    send_email("Heat Lamp Turned OFF ❄️", "The heat lamp has been switched OFF.", [TO_EMAIL])
    return redirect(url_for("dashboard"))


# -------------------- EDIT SCHEDULE --------------------

@app.route("/edit_schedule", methods=["GET", "POST"])
def edit_schedule():
    if "username" not in session:
        flash("Please log in first", "warning")
        return redirect(url_for("login"))

    if request.method == "POST":
        schedule = schedule_db.get_schedule()
        for day in schedule.keys():
            open_time = request.form.get(f"{day}_open")
            close_time = request.form.get(f"{day}_close")
            if open_time and close_time:
                schedule_db.update_schedule(day, open_time, close_time)
        flash("Weekly schedule updated successfully!", "success")
        return redirect(url_for("dashboard"))

    # Load current schedule
    schedule = schedule_db.get_schedule()
    return render_template("edit_schedule.html", schedule=schedule)



# -------------------- STATUS API --------------------

@app.route("/status")
def status():
    if "username" not in session:
        return jsonify({"error": "Unauthorized"}), 403

    city = session.get("weather_city", None)
    return jsonify({
        "gate_status": state.get_state(),
        "lamp_status": heat_lamp_state.get_state(),
        "weather": get_weather(city),
        "logs": logs_db.read_logs(10),
        "schedule": schedule_db.get_schedule()
    })


# -------------------- RUN APP --------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
