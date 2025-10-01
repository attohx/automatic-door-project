from flask import Flask, render_template, redirect, url_for
from config import EMAIL, TO_EMAIL
from mail import mail, send_email
from weather import get_weather
from flask import jsonify
import state
import logs_db
import db_setup

app = Flask(__name__)
app.config.update(EMAIL)
mail.init_app(app)

dbstart = db_setup.kreatedb()


@app.route("/")
def dashboard():
    try:
        dbstart
    except:
        print ("Error. Database could not be created")

    finally:
            
        gate_status = state.get_state()
        weather = get_weather() #fetches weather data
        recent_logs = logs_db.read_logs(10)
        return render_template("dashboard.html",gate_status =gate_status, weather = weather, logs = recent_logs)




@app.route("/open")
def open_gate():
    if state.get_state() =="OPEN":
        return "Gate is already Open!"
    
    # GPIO code for opening gate would go here
    state.set_state("OPEN")
    logs_db.log_action("OPENED","user") #add to log db
    send_email("Poultry Gate Opened 🟢", "The poultry gate has been opened.", [TO_EMAIL])
    return redirect(url_for("dashboard"))

@app.route("/close")
def close_gate():
    if state.get_state() =="CLOSED":
        return "Gate is already Closed!"
    
    # GPIO code for closing gate would go here
    state.set_state("CLOSED")
    logs_db.log_action("CLOSED", 'user') #log to db
    send_email("Poultry Gate Closed 🔴", "The poultry gate has been closed.", [TO_EMAIL])
    return redirect(url_for("dashboard"))


@app.route("/status")
def status():
    return jsonify({
        "gate_status": state.get_state(),
        "weather": get_weather(),
        "logs": logs_db.read_logs(10)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

