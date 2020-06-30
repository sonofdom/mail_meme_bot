#import all libraries needed
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
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

def Create_message(to_emails,img_name,img_path,text, subject = "Daily Meme",from_email = f"<{username}>"):
    #Brings up an error if to_emails is not a list
    assert isinstance(to_emails, list)
    msg = MIMEMultipart("alternative")
    msg["From"] = from_email
    #turns it from list [] to list ,x,x, etc
    msg["To"] = ",".join(to_emails)
    msg["subject"] = subject

    #word part of an email
    txt_part = MIMEText(text,"plain")
    msg.attach(txt_part)
    
    #add the image
    img_data = open(img_path, 'rb').read()
    atch_img = MIMEImage(img_data,img_path )
    msg.attach(atch_img)

    #format msg?
    msg = msg.as_string()
    print(msg)
    return msg


def send(msg,to_emails,text):
    #login to my smto server
    server = smtplib.SMTP(host = "smtp.gmail.com",port = 587)
    server.ehlo()
    #creates secure connection
    server.starttls()
    #logs in
    server.login(username, password)
    print(server.login(username, password))
    server.sendmail(text,from_email, to_emails, msg)
    print("Message sent")
    #close service
    server.quit()

def main(img_name,img_path):
    text = "Hi"
    to_emails  = to_email_list()
    msg = Create_message(to_emails,img_name,img_path,text)
    print("message Created")
    send(msg,to_emails,text)
    return "Email sent"

if __name__ == "__main__":
    main()

