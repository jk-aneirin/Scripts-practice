import re
def fuzzyfinder(user_input,collection):
    suggestions=[]
    pattern='.*?'.join(user_input) //使用非贪婪匹配
    regex=re.compile(pattern)
    for item in collection:
        match=regex.search(item)
        if match:
            suggestions.append((len(match.group()),match.start(),item))
    return [x for _,_,x in sorted(suggestions)]

