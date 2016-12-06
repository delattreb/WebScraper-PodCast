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


class Mail:
    def __init__(self):
        conf = com_config.Config()
        self.config = conf.getconfig()
    
    def send_mail_gmail(self, subject, table, filename = ''):
        htmlheader = """\
            <html>
              <head></head>
              <body>
                <H2>Nouvelles informations</H2><br><br>
                <p>
            """
        
        htmlfooter = """\
                </p>
              </body>
            </html>
            """
        
        for line in table:
            htmlheader += line + "<br>"
        htmlheader += htmlfooter
        
        msg = MIMEMultipart()
        msg['To'] = self.config['EMAIL']['to']
        msg['From'] = self.config['EMAIL']['from']
        msg['Subject'] = subject
        msg.attach(MIMEText(htmlheader, 'html'))
        
        if filename:
            attachment = open("./" + filename, "rb")
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
            msg.attach(part)
  
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.config['EMAIL']['from'], self.config['EMAIL']['password'])
        text = msg.as_string()
        server.sendmail(self.config['EMAIL']['from'], self.config['EMAIL']['to'], text)
        server.quit()
        
        logger = com_logger.Logger('Mail')
        logger.info('Mail sent')

