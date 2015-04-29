def process(stack):
    
    size=len(stack)
            
    w=[0 for i in range(size+1)]]
    p=[0 for i in range(size+1)]] 
    w[1]=stack[size-1]
    w[2]=w[1]+stack[size-2]
    w[3]=w[2]+stack[size-3]
    p[1]=0
    
    print stack


def main():    
    T = int(raw_input())
    for i in xrange(T):
        N = int(raw_input())
        stack = map(int,raw_input().split(" "))
        process(stack)
        

print main()
