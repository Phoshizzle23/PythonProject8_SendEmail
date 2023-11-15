# Python Automation Project 3 - Send Email (Basic Plain Text)
# mattdummy73@gmail.com
# Batman69
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, receiver_email, subject, message):
    try:
        # Set up the SMTP server
        smtp_server = "smtp.gmail.com"
        smtp_port = 587  # For TLS encryption

        # Create a secure connection to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        # Create a message
        email_message = MIMEMultipart()
        email_message["From"] = sender_email
        email_message["To"] = receiver_email
        email_message["Subject"] = subject

        # Attach the message body
        email_message.attach(MIMEText(message, "plain"))

        # Send the email
        server.send_message(email_message)

        # Close the connection to the SMTP server
        server.quit()

        print("Email sent successfully!")
    except Exception as e:
        print("An error occurred while sending the email:", e)

def main():
    # Email configuration
    sender_email = "mattdummy73@gmail.com" # your_email@gmail.com
    sender_password = "P@ssword89!!!" #your_password
    receiver_email = "mattywoodward88@gmail.com" # recipient_email@example.com
    subject = "Hello from Python!"
    message = "This is a test email sent using Python."

    # Send the email
    send_email(sender_email, sender_password, receiver_email, subject, message)

if __name__ == "__main__":
    main()
