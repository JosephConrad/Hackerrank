import math

def is_power2(num):
    return num != 0 and ((num & (num - 1)) == 0)

for i in range(input()):
    N=int(raw_input())
    i=0
    while N>1:
        print N
        if not is_power2(N):
            a = int(math.floor(math.log(N,2)))
            N^=pow(2,a)
        else:
            N>>=1 
        i+=1
        print N
    print ['Richard', 'Louise'][i%2]

    
