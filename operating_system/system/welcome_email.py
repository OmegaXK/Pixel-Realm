"""Send the user an email congratulating them on starting their
journy with Pixel Realm."""

# Imports.
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def email_main(receiver):
    """Configure, build, and send the email."""

    configure_email(receiver)
    message = build_email()
    send_email(message)
    print('A welcome email was sent to your inbox.')


def configure_email(email_address):
    "Create the email."
    global sender_email, receiver_email, subject, body

    sender_email = "omegaxk314@gmail.com"
    receiver_email = str(email_address)
    subject = 'Welcome to Pixel Realm!'
    body = """
    Thank you for downloading Pixel Realm. We hope that you 
    have a good experience with this amazing app. 
    
    If you are interested in learning more about Pixel Realm and 
    customizing it for your own needs, make sure to check out the 
    pixel_realm_guide.txt file in the information folder. 
    
    While in the information folder, you should also take a look at the 
    credits.txt file, which contains information about the software and 
    websites we use to make applications like Pixel Realm, and all of the 
    sounds and images used in the project.

    Thanks again!

    - Omega Devlopment Team
    Pixel Realm
    """
    return


def build_email():
    """Create the MIME message."""

    # Make the message.
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject 

    # Attach the body to the email.
    message.attach(MIMEText(body, "plain"))
    return message


def send_email(message):
    """Connect to Gmail and send the email."""

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls() # Start TLS encryption.
        server.login(sender_email, "laue cenp wiwo ixzk")
        
        server.sendmail(sender_email, receiver_email, message.as_string())
        return
    

if __name__ == "__main__": # Testing purposes.
    email_main('omegaxk314@gmail.com')