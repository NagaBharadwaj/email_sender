import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'  # Change to your SMTP server
SMTP_PORT = 587  # Use 465 for SSL
SENDER_EMAIL = os.getenv('SENDER_EMAIL')
SENDER_PASSWORD = os.getenv('SENDER_PASSWORD')

# Read recipient data from CSV
recipients_df = pd.read_csv('recipients.csv')

# Create the SMTP session
def send_email(to_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()  # Use server.starttls() for TLS; use server.login() directly for SSL
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, to_email, msg.as_string())

# Compose and send personalized emails
for index, row in recipients_df.iterrows():
    recipient_email = row['email']
    recipient_name = row['name']

    # Create personalized email content
    subject = f"Hello, {recipient_name}!"
    body = f"Dear {recipient_name},\n\nThis is a personalized email just for you!\n\nBest regards,\nYour Company"

    # Send the email
    send_email(recipient_email, subject, body)
    print(f"Email sent to {recipient_name} at {recipient_email}")

print("All emails have been sent successfully!")
