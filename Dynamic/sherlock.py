def printf(lists, l):
    for l in lists:
        print '\t'.join(map(lambda x: str(x), l))
    print '\t'.join(map(lambda x: str(x), range(len(l))))
    print '\t'.join(map(lambda x: str(x), l))

def process(l, n):
    dp = [[0 for _ in range(n)] for _ in range(2)]
    
    for i in range(1, n):
        d1=abs(l[i]-1) 
        d2=abs(l[i]-l[i-1])
        dp[0][i]=max(d1+dp[1][i-1], d2+dp[0][i-1])
        dp[1][i]= dp[0][i-1]+abs(l[i-1]-1)

    print max(dp[0][n-1], dp[1][n-1])

def main():
    for i in xrange(input()):
        n = int(raw_input())
        l=map(int, raw_input().split(" "))
        process(l, n) 

main()
