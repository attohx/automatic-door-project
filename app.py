from flask import Flask, render_template, redirect, url_for
from config import EMAIL
from mail import mail, send_email

app = Flask(__name__)
app.config.update(EMAIL)
mail.init_app(app)

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/open")
def open_gate():
    # GPIO code for opening gate would go here
    send_email("Poultry Gate Opened 🟢", "The poultry gate has been opened.", ["attohnathanan@gmail.com"])
    return redirect(url_for("dashboard"))

@app.route("/close")
def close_gate():
    # GPIO code for closing gate would go here
    send_email("Poultry Gate Closed 🔴", "The poultry gate has been closed.", ["attohnathanan@gmail.com"])
    return redirect(url_for("dashboard"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

