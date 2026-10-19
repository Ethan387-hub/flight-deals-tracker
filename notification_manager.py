import smtplib
import os
from dotenv import load_dotenv
load_dotenv()
EMAIL = os.getenv("GMAIL_ADDRESS")
PASSWORD = os.getenv("APP_PASSWORD")
RECIPIENT = os.getenv("RECIPIENT_EMAIL")
class NotificationManager:
    def __init__(self):
        self.email = EMAIL
        self.password = PASSWORD
        self.recipient = RECIPIENT
    def send_email(self,message):
        with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
            connection.starttls()
            connection.login(user=self.email,password=self.password)
            connection.sendmail(
                from_addr=self.email,
                to_addrs=self.recipient,
                msg=f"Subject: Flight deal found\n\n{message}"
            )
