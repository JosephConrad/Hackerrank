def process(N, p):
    maxP=[p[-1]]
    i=len(p)-2
    while i>=0:
        if p[i]>maxP[0]: maxP.insert(0,p[i])
        else:
             maxP.insert(0,maxP[0])
        i-=1
        
    cost,profit,shares = 0,0,0
    if maxP[0]==maxP[1]:
        shares=1
        cost=p[0]
    for i in range(1, len(p)-1):
        if maxP[i]==maxP[i+1]: 
            shares+=1
            cost+=p[i]
        else:
            profit+=shares*p[i]-cost 
            shares,cost = 0,0
    return profit+shares*p[-1]-cost


def main():    
    T = int(raw_input())
    for i in xrange(T):
        N = int(raw_input())
        p = map(int, raw_input().split(" "))
        print process(N, p)
        
main()
