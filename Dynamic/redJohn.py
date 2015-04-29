
N=40

def process(tab):
    tab[0], tab[1], tab[2] = 1,1,1
    tab[3]=2
    for i in range(4, N):
        tab[i]=tab[i-1]+tab[i-4]

def sieve(numbers, n):
    for prime in numbers:
        if prime < 2:
            continue
        if prime > n ** 0.5:
            break
        for i in range(prime ** 2, n+1, prime):
            numbers[i] = 0

def main():    
    T = int(raw_input())
    tab = [0 for _ in range(0,N)]
    process(tab)
    
    primes=range(0,tab[N-1]+1)
    sieve(primes, tab[N-1])
    counter = [0 for _ in range(len(primes))]
    counter[2]=1
    for i, elt in enumerate(primes):
        if i<3: continue
        counter[i]=counter[i-1]
        if elt!=0: counter[i]+=1
    for i in xrange(T):
        n = int(raw_input())
        comb = tab[n-1]
        print counter[comb]
        
        #stack = map(int,raw_input().split(" "))
        #print stack 
    
            

main()
