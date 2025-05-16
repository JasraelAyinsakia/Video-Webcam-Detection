import smtplib
import imghdr
from email.message import EmailMessage

PASSWORD = "gfppmjthbktihnlu"
SENDER = "apuseyinejake011@mial.com"
RECEIVER = "apuseyinejake011@gmail.com"


def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up!"
    email_message.set_content("Hey, we just got a new customer!")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    try:
        # Try with SSL first (most reliable)
        gmail = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        gmail.login(SENDER, PASSWORD)
        gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
        gmail.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
        # Fallback to TLS
        try:
            gmail = smtplib.SMTP("smtp.gmail.com", 587)
            gmail.ehlo()
            gmail.starttls()
            gmail.login(SENDER, PASSWORD)
            gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
            gmail.quit()
            print("Email sent successfully using TLS fallback!")
        except Exception as e2:
            print(f"Both SSL and TLS failed: {e2}")

if __name__ == "__main__":
    send_email(image_path="images/10.png")
