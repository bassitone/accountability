#!/usr/bin/python3

from flask import Flask
from flask_mail import Mail, Message

app =Flask(__name__)
mail=Mail(app)

app.config.update(
   DEBUG=False,
      #EMAIL SETTINGS
        MAIL_SERVER='smtp.gmail.com',
        MAIL_PORT=465,
        MAIL_USE_SSL=True,
        MAIL_USERNAME = 'email_here',
        MAIL_PASSWORD = "password_here"
        )

mail=Mail(app)

@app.route("/")
def index():
	msg = Message(
              'Hello',
	       sender='my_email',
	       recipients=
               ['receiver_email'])
	msg.body = "This is the test flask email!"
	mail.send(msg)
	return "Sent"

if __name__ == "__main__":
    app.run()
