n = int(raw_input())
tab = map(int, raw_input().split(" "))
m = len(tab)
result = 0
for i in range(m-1):
    counter = 0
    for j in range(i+1, m):
        if tab[j] > tab[i]: counter += 1
        if tab[j] < tab[i]: result += counter
print result
