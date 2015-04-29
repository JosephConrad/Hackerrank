import re

n = int(raw_input())
l = list()
for i in range(n):
    l.append(str(raw_input()))

def valid(mail):
    x = not re.match(r"^[a-zA-Z0-9-_]+\@[a-zA-Z0-9]+\.[a-zA-Z]{3,}$", mail) == None
    print x
    return x
    
l1=filter(lambda x: valid(x),l)
print l1
l2=sorted(l1)
print l2


