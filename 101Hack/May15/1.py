string = list(raw_input())
i = 1
while True:
    if len(string) > 1 and string[0] == string[1]:
        string.pop(0)
    else:
        break
        
ile = len(set(string))
count = dict()
for i in set(string):
    count[i] = 0
array = ile * [0]
for letter in string:
    count[letter] = count[letter] + 1
result = 1
for elt in count.values():
    result *= elt
print result % 1000
