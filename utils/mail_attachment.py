#!/usr/bin/env python
'''send mail including attachment'''
import email
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import encoders
import smtplib
import mimetypes

_user='xxxx@qq.com'
_pwd='dajekajkfjkejfa'

from_addr='xxxxxx@qq.com'
to_addr='xxxxxx@163.com'
subject_header='With attachment'
attachment='x.txt'
body='''
This message includes attachment
'''

m=MIMEMultipart()
m['To']=to_addr
m['From']=from_addr
m['Subject']=subject_header

ctype,encoding=mimetypes.guess_type(attachment)
print ctype,encoding
maintype,subtype=ctype.split('/',1)
print maintype,subtype

m.attach(MIMEText(body))
fp=open(attachment,'rb')
msg=MIMEBase(maintype,subtype)
msg.set_payload(fp.read())
fp.close()
encoders.encode_base64(msg)
msg.add_header('Content-Disposition',"attachment",filename=attachment)
m.attach(msg)

s=smtplib.SMTP_SSL('smtp.qq.com',465)
s.set_debuglevel(1)
s.login(_user,_pwd)
s.sendmail(from_addr,to_addr,m.as_string())
s.quit()

