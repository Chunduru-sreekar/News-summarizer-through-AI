import smtplib, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "srikarch285@gmail.com"
    password = os.getenv("EMAIL_APP_PASSWORD")

    receiver = "sreekarseshasaichunduru@gmail.com"
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, message)
            print("Email sent successfully!")

    except smtplib.SMTPAuthenticationError:
        print("Authentication failed. check your username and password environment variable.")
    except Exception as e:
        print(f"An error occurred:{e}")
send_email("how are you today?")



