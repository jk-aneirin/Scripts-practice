import smtplib
from email.mime.text import MIMEText
_user='xxxx@qq.com'
_pwd='asdfaje3aasak12jk2' #turn on IMAP/SMTP service,The string is authorization code
_to='xxxx@163.com'

msg=MIMEText('Test')
msg['Subject']='Mail test'
msg['From']=_user
msg['To']=_to

try:
    s=smtplib.SMTP_SSL('smtp.qq.com',465)
    s.login(_user,_pwd)
    s.sendmail(_user,_to,msg.as_string())
    s.quit()
    print 'Success!'
except smtplib.SMTPException,e:
    print "Failed,%s"%e
