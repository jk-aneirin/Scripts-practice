import re
m=re.search(r'\bthe','bite the dog')
if m:
    print m.group() #output:the
--------------------------------------
m=re.search(r'\Bthe','bitethe dog')
if m:
    print m.group() #output:the
--------------------------------------
s='This and that.'
print re.findall(r'(th\w+) and (th\w+)',s,re.I) #output:[('This', 'that')]
---------------------------------------
re.sub('[ae]', 'X', 'abcdef')#output:XbcdXf
---------------------------------------
bool(re.search(r'(?:(x)|y)(?(1)y|x)', 'xy')) #output:True
bool(re.search(r'(?:(x)|y)(?(1)y|x)', 'yx')) #output:True
---------------------------------------
re.findall(r'\w+(?= van Rossum)',
        '''
        Guido van Rossum
        Tim Peters
        Alex Martelli
        Just van Rossum
        Raymond Hettinger
        ''')
#output:['Guido', 'Just']
---------------------------------------


