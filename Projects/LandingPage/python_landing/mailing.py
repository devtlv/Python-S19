import flask_mail
from python_landing import app, mail_mgr

def send_mail(subject, recipients, text, html):
    msg = flask_mail.Message(
        subject=subject,
        sender=app.config['MAIL_USERNAME'],
        recipients=recipients,
        text=text,
        html=html
    )

    mail_mgr.send(msg)

