import os
import smtplib
from email.mime.text import MIMEText

clear = lambda: os.system("clear")

def send_mail(message, sender, password):
    reciver = input("Mail: ")

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)

        msg = MIMEText(message)
        subj = input("Enter Subject Of Message: ")
        msg["Subject"] = subj

        server.sendmail(sender, reciver, msg.as_string())
        clear()
        return "Message Was sended!"

    except Exception:
        clear()
        return "Sorry, But something went wrong :(\n" \
               "Please, Check your login/Password"

def main():
    message = input("Enter text that you want to send: ")
    sender = input("Enter your MAIL: ")
    password = input("Enter your PASSWORD: ")

    print(send_mail(message, sender, password))

if __name__ == '__main__':
    main()