def solve(a,b,n):
    for i in range(n-2):
        x = b
        b = a + b*b
        a = x
    print b
        
a,b,n = [ int(i) for i in raw_input().strip().split() ]  
solve(a,b,n)
