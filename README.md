# Personalized Email Sender Script

This repository contains a Python script that automates the process of sending personalized emails to a list of recipients. The script is designed to streamline communication and engagement by allowing users to tailor the content of each email based on individual preferences and details.

## Features

- Sends personalized emails to multiple recipients.
- Reads recipient details from a CSV file.
- Uses environment variables to securely store email credentials.

## Prerequisites

- Python 3.x
- pandas library

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/NagaBharadwaj/email_sender.git
   cd email_sender

   
## Install the required Python packages:
pip install pandas

## Set up environment variables:
Set your email credentials as environment variables. This step helps to keep your credentials secure.

### Windows:
Open Command Prompt and run:
setx SENDER_EMAIL "your_email@gmail.com"
setx SENDER_PASSWORD "your_password_or_app_password"

### macOS/Linux:
Open Terminal and run:
export SENDER_EMAIL="your_email@gmail.com"
export SENDER_PASSWORD="your_password_or_app_password"


## Usage
Prepare the recipient CSV file:
Create a file named recipients.csv in the project directory with the following format:

email,name
example1@example.com,Naga
example2@example.com,Bharadwaj

## Run the script:
Open a terminal in the project directory and run:
python email_sender.py

## Script Details

import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
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
        server.starttls()  # Secure the connection
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

## Notes
Ensure that your email provider allows SMTP access and that you have enabled the necessary settings (e.g., "Less secure app access" for Gmail or using an App Password).
Handle email credentials securely. Consider using a more secure method for managing sensitive information in a production environment.
