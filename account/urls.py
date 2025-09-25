import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
de send_email(recipient_email, subject, message_body):
try:
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "your_email@gmail.com"
    password = "your_password"
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message_body, 'plain'))
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()
    server.login(sender_email, password)
    text = msg.as_string()
    server.sendmail(sender_email, recipient_email, text)
    server.quit()
    print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")