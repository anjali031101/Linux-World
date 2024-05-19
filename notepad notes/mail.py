def run():

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart()

msg['From'] = 'sender'

msg['To'] = 'recvr'

msg['Subject'] = 'Email using Python'

message = 'hi'

msg.attach(MIMEText(message))

mailserver = smtplib.SMTP('smtp.gmail.com', 587)

mailserver.ehlo()

mailserver.starttls()

mailserver.ehlo()

mailserver.login('sender', 'passwd')

mailserver.sendmail('sender', 'recvr', msg.as_string())

mailserver.quit()
