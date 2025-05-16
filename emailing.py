import smtplib
import mimetypes
from email.message import EmailMessage

PASSWORD = "gfppmjthbktihnlu"  # Your App Password
SENDER = "apuseyinejake011@gmail.com"
RECEIVER = "apuseyinejake011@gmail.com"

def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up!"
    email_message["From"] = SENDER
    email_message["To"] = RECEIVER
    email_message.set_content("Hey, we just got a new customer!")

    # Detect MIME type
    mime_type, _ = mimetypes.guess_type(image_path)
    maintype, subtype = mime_type.split('/')

    # Attach image
    with open(image_path, "rb") as file:
        content = file.read()
        email_message.add_attachment(content, maintype=maintype, subtype=subtype, filename=image_path)

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(SENDER, PASSWORD)
            smtp.send_message(email_message)
            print("Email sent successfully using TLS!")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    send_email(image_path="images/10.png")
