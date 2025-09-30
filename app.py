from flask import Flask, render_template, redirect, url_for
from config import EMAIL
from mail import mail, send_email
from weather import get_weather
import state

app = Flask(__name__)
app.config.update(EMAIL)
mail.init_app(app)

@app.route("/")
def dashboard():
    gate_status = state.get_state()
    weather = get_weather() #fetches weather data
    return render_template("dashboard.html",gate_status =gate_status, weather = weather)



@app.route("/open")
def open_gate():
    if state.get_state() =="OPEN":
        return "Gate is already Open!"
    
    # GPIO code for opening gate would go here
    state.set_state("OPEN")
    send_email("Poultry Gate Opened 🟢", "The poultry gate has been opened.", ["attohnathanan@gmail.com"])
    return redirect(url_for("dashboard"))

@app.route("/close")
def close_gate():
    if state.get_state() =="CLOSED":
        return "Gate is already Closed!"
    
    # GPIO code for closing gate would go here
    state.set_state("CLOSED")
    send_email("Poultry Gate Closed 🔴", "The poultry gate has been closed.", ["attohnathanan@gmail.com"])
    return redirect(url_for("dashboard"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

