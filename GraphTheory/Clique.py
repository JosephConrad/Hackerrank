l = map(int,raw_input().split())

def process(n, m):
    edges=range(n-1,-1,-1)
    print edges
    total=0
    for i in range(0,n):
        total+=edges[i]
        if total>=m:
            return i+2
 
for i in xrange(l[0]):
    n,m = map(int,raw_input().split())
    print process(n, m)
