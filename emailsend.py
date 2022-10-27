from email.message import EmailMessage
# from passw import password

import ssl
import smtplib

email_sender = 'brianaginga35@gmail.com'
email_password = 'gvzillvwlvbrknin'

email_reciever  =  'nedoc52824@cadolls.com'

subject = 'Thursday'

body = '''

Boom

'''

em = EmailMessage()

em['From'] = email_sender
em['To'] = email_reciever
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smpt.gamail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())



 