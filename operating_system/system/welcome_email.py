"""Send the user an email congratulating them on starting their
journy with Pixel Realm."""

# Imports.
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(email_address):
    """Send the welcome email to the user."""


def configure_email(email_address):
    "Create the email."

    sender_email = "omegaxk314@gmail.com"
    receiver_email = str(email_address)
    subject = 'Welcome to Pixel Realm!'
    body = 'Placeholder hi hello hi this is a placeholder'


def create_message():
    """Create the MIME message."""