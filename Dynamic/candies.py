


def dp(c):
    res=[1]
    for i in range(1,len(c)):
        if c[i]<=c[i-1]: res.append(1)
        else:
            res.append(res[i-1]+1)
    return res

def process(c):
    res1=dp(c)
    res2=dp(c[::-1])[::-1]
    res=[]
    for i, j in zip(res1, res2):
        res.append(max(i,j)) 
    print sum(res)
    
def main():    
    T = int(raw_input())
    c = []
    for i in xrange(T):
        c.append(int(raw_input()))
    process(c)
        
main()
