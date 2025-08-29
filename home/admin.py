import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def send_confirmation_email(user_email, hardcoded_email="example@example.com"):
    sender_email = hardcoded_email
    sender_pssword = "your_password"
    receiver_emai = user_email
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["subject"] = "Contact from submission confirmation"
    body = "dear user,/n/nThankyou for submitting our contact form.we have received your message and will get back to you  soon /n/nbest regards,/n[your name]"
    message.attach(MIMEText(body, "plain"))
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print("confirmation email sent successfully!")
     except Exception as e:
        print("error sending confirmation email:" str(e))
        if __name__ == "__main__":
            user_email = "user@example.com"
            send_confirmation_email(user_email)   