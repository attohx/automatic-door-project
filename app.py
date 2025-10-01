from flask import Flask, render_template, redirect, url_for, request, session, flash, jsonify
from config import EMAIL, TO_EMAIL, ADMIN_USERNAME, ADMIN_PASSWORD, SECRET_KEY, PINS
from mail import mail, send_email
from weather import get_weather
import state
import logs_db
import db_setup
import door

app = Flask(__name__)
app.config.update(EMAIL)
app.secret_key = SECRET_KEY
mail.init_app(app)

dbstart = db_setup.kreatedb()

#-----------------------DOOR CONFIG---------
my_door = door.Door(PINS["SERVO"])
#-------------------------------------------

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
        print("Error. Database could not be created")
    finally:
        gate_status = state.get_state()
        weather = get_weather()
        recent_logs = logs_db.read_logs(10)
        return render_template("dashboard.html", gate_status=gate_status, weather=weather, logs=recent_logs)

# -------------------- GATE CONTROLS --------------------

@app.route("/open")
def open_gate():
    if "username" not in session:
        return redirect(url_for("login"))

    if state.get_state() == "OPEN":
        flash("Gate is already Open!", "info")
        return redirect(url_for("dashboard"))

    state.set_state("OPEN")
    my_door.open()
    logs_db.log_action("OPENED", session["username"])
    send_email("Poultry Gate Opened 🟢", "The poultry gate has been opened.", [TO_EMAIL])
    return redirect(url_for("dashboard"))

@app.route("/close")
def close_gate():
    if "username" not in session:
        return redirect(url_for("login"))

    if state.get_state() == "CLOSED":
        flash("Gate is already Closed!", "info")
        return redirect(url_for("dashboard"))

    state.set_state("CLOSED")
    my_door.close()
    logs_db.log_action("CLOSED", session["username"])
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
        "logs": logs_db.read_logs(10)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

#-----------------------DOOR CLEANUP---------
my_door.cleanup()
#-------------------------------------------