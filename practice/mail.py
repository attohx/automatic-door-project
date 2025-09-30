from flask import Flask
from flask_mail import Mail, Message
import config

app = Flask(__name__)

app.config.update(config.EMAIL)


mail = Mail(app)

@app.route('/')
def send_email():
    try:
        msg = Message (subject='Hello!',recipients=['attohnathanan@gmail.com'], body = 'This a test email sent from Flask-Mail!')

        mail.send(msg)
        return 'Email Sent succesfully!'

    except Exception as e:
        return f"Error sending email: {e}"    

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True) 