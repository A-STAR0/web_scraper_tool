import os
import smtplib
from email.mime.text import MIMEText
from typing import List
from .notification_strategy import NotificationStrategy
import logging

logger = logging.getLogger(__name__)


class EmailNotification(NotificationStrategy):
    def __init__(self, email_addresses: List[str]):
        self.email_addresses = email_addresses

    @staticmethod
    def send_email(to_addresses, subject, body):
        logger.info(f"Sending email to {', '.join(to_addresses)}: {subject} - {body}")
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = os.getenv('EMAIL_ID')
        msg['To'] = ', '.join(to_addresses)

        # we can replace it with our SMTP server details, we can even integrate slack to send message
        with smtplib.SMTP(os.getenv('SMTP_SERVER')) as server:
            server.login(os.getenv('EMAIL_ID'), os.getenv('PASSWORD'))
            server.sendmail(os.getenv('EMAIL_ID'), to_addresses, msg.as_string())

    def notify(self, message: str):
        self.send_email(self.email_addresses, "Scraping Status", message)

