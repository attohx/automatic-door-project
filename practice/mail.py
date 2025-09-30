from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'quayeadelaide18@gmail.com'
app.config['MAIL_PASSWORD'] = 'gksv gvgh duiv ipbq'
app.config['MAIL_DEFAULT_SENDER'] = 'quayeadelaide18@gmail.com'

mail = Mail(app)

app.route('/')
def send_email():
    msg = Message ('Hello!', recipients=['attohnathanan@gmail.com'], body = 'This a test email sent from Flask-Mail!')

    mail.send(msg)
    return 'Email Sent succesfully!'