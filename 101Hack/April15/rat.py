n = int(raw_input())
speed = map(int, raw_input().split(" "))
distance = map(int, raw_input().split(" "))
result = []
for i in range(len(speed)):
    result.append(float(distance[i])/float(speed[i]))
maks = 100000.0
for i in range(len(speed)):
    if result[i] < maks:
        maks = result[i]

for i in range(len(speed)):
    if result[i] == maks:
        print i+1
