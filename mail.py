from flask_mail import Mail, Message

mail = Mail()

def send_email(subject, body, recipients):
    try:
        msg = Message(subject=subject, recipients=recipients, body=body)
        mail.send(msg)
        return True
    except Exception as e:
        print(f"Error sending alert: {e}")
        return False
