#import all libraries needed
import os
import smtplib
import imghdr
from email.message import EmailMessage
from config import username, password


from_email = username

def to_email_list():
    e_list = []
    with open("email_list.txt","r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            e_list.append(str(line))
    return e_list

def Create_message(to_emails,img_name,img_path,from_email = f"<{username}>"):
    msg = EmailMessage()
    msg['Subject'] = "Check out todays Daily Meme"
    msg['From'] = from_email
    msg['To'] = to_emails
    msg.set_content("Image Attatched")

    with open(str(img_path),'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = str(img_name)

    msg.add_attachment(file_data,maintype='image',subtype=file_type,filename=file_name)
    return msg


def send(msg):
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(username,password)
        smtp.send_message(msg)

def main(img_name,img_path):
    to_emails  = to_email_list()
    msg = Create_message(to_emails,img_name,img_path)
    send(msg)
    return "Email sent"

if __name__ == "__main__":
    main()

