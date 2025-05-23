import smtplib, ssl
import os
from dotenv import load_dotenv

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "mikebstudy@gmail.com"

    load_dotenv(override=True)
    password = os.getenv("PMC_02_SHOWCASE_PW")

    context = ssl.create_default_context()

    receiver = "mikebstudy@gmail.com"

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)