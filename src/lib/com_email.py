"""
com_email.py v1.0.0
Auteur: Bruno DELATTRE
Date : 07/08/2016
"""

import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from lib import com_config, com_logger


def send_mail_gmail(subject, table, filename=""):
    config = com_config.getConfig()
    body = "<H2>Nouvelles informations</H2><br><br>"

    for line in table:
        body += line + "<br>"

    msg = MIMEMultipart()

    msg['From'] = config['EMAIL']['from']
    msg['To'] = config['EMAIL']['to']
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'html'))

    if len(filename) > 0:
        attachment = open("./" + filename, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(config['EMAIL']['from'], config['EMAIL']['password'])
    text = msg.as_string()
    server.sendmail(config['EMAIL']['from'], config['EMAIL']['to'], text)
    server.quit()
    
    logger = com_logger.Logger('Mail')
    logger.info('Mail sent')
