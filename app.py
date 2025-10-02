# app.py
from flask import Flask, render_template, redirect, url_for, request, session, flash, jsonify
from config import EMAIL, TO_EMAIL, ADMIN_USERNAME, ADMIN_PASSWORD, SECRET_KEY
from mail import mail, send_email
from weather import get_weather
import state
import logs_db
import db_setup
import schedule_db
from scheduler import init_scheduler, schedule_jobs
import atexit

app = Flask(__name__)
app.config.update(EMAIL)
app.secret_key = SECRET_KEY
mail.init_app(app)

# Init DBs
db_setup.kreatedb()
schedule_db.init_schedule_db()

# Init scheduler
scheduler = init_scheduler(app)

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

    gate_status = state.get_state()
    weather = get_weather()
    recent_logs = logs_db.read_logs(10)
    sched = schedule_db.get_schedule() or {"open_time": "--:--", "close_time": "--:--"}

    return render_template("dashboard.html",
                           gate_status=gate_status,
                           weather=weather,
                           logs=recent_logs,
                           schedule=sched)

# -------------------- UPDATE SCHEDULE --------------------

@app.route("/update_schedule", methods=["POST"])
def update_schedule_route():
    if "username" not in session:
        flash("Please log in first", "warning")
        return redirect(url_for("login"))

    open_time = request.form.get("open_time")
    close_time = request.form.get("close_time")

    if not open_time or not close_time:
        flash("Invalid schedule format", "danger")
        return redirect(url_for("dashboard"))

    schedule_db.update_schedule(open_time, close_time)
    schedule_jobs(app)  # refresh scheduler jobs
    flash(f"Schedule updated: {open_time} → {close_time}", "success")
    return redirect(url_for("dashboard"))

# -------------------- GATE CONTROLS --------------------

@app.route("/open")
def open_gate():
    if "username" not in session:
        return redirect(url_for("login"))

    if state.get_state() == "OPEN":
        flash("Gate is already open", "info")
        return redirect(url_for("dashboard"))

    state.set_state("OPEN")
    logs_db.log_action("OPENED", session.get("username", "user"))
    send_email("Poultry Gate Opened 🟢", "The poultry gate has been opened.", [TO_EMAIL])
    return redirect(url_for("dashboard"))

@app.route("/close")
def close_gate():
    if "username" not in session:
        return redirect(url_for("login"))

    if state.get_state() == "CLOSED":
        flash("Gate is already closed", "info")
        return redirect(url_for("dashboard"))

    state.set_state("CLOSED")
    logs_db.log_action("CLOSED", session.get("username", "user"))
    send_email("Poultry Gate Closed 🔴", "The poultry gate has been closed.", [TO_EMAIL])
    return redirect(url_for("dashboard"))

# -------------------- STATUS API --------------------

@app.route("/status")
def status():
    if "username" not in session:
        return jsonify({"error": "Unauthorized"}), 403

    return jsonify({
        "gate_status": state.get_state(),
        "weather": get_weather(),
        "logs": logs_db.read_logs(10),
        "schedule": schedule_db.get_schedule()
    })

# -------------------- CLEANUP --------------------

# shutdown scheduler on exit
atexit.register(lambda: scheduler.shutdown(wait=False))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
