#!/usr/bin/env python3
import hmac
import random

def hmac_md5(key,s):
    return hmac.new(key.encode('utf-8'),s.encode('utf-8'),'MD5').hexdigest()

class User():
    def __init__(self,username,password):
        self.username = username
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = hmac_md5(self.key,password)

db = {
        'michael':User('michael','123456'),
        'bob':User('bob','abc999'),
        'alice':User('alice','alice2008'),
        }

def login(username,password):
    user = db[username]
    return user.password == hmac_md5(user.key,password)

assert login('michael', '123456')
