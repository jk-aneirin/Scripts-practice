import poplib
username='XXXXX@qq.com'
password='password'
mail_server='pop.qq.com'
p=poplib.POP3_SSL(mail_server)
p.user(username)
p.pass_(password)
numMessages=len(p.list()[1])
for i in range(numMessages):
    for j in p.retr(i+1)[1]:
        print j
p.quit()
