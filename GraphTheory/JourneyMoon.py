parent = []
ile = []

def find(elt):
    if parent[elt]==elt: return elt
    eltParent=find(parent[elt])
    parent[elt]=eltParent
    return eltParent

def union(a, b):
    fa=find(a)
    fb=find(b)

    if fa==fb: return False
    if ile[fa]<=ile[fb]:
        ile[fb]+=ile[fa]
        parent[fa]=fb
    else:
        ile[fa]+=ile[fb]
        parent[fb]=fa
    
    return True
    
def factorial(n):
    if n==1: return 1
    return n*factoria(n-1)
    

def main():
    N,l = map(int,raw_input().split())
    for i in range(0,N):
        parent.append(i)
        ile.append(1)
    for i in xrange(l):
        a,b = map(int,raw_input().split())
        union(a,b)
    
    single = dict()
    for elt in parent:
        rep=find(elt)
        if not rep in single:
            single[rep]=ile[rep]
    result=0
    total=reduce(lambda a, b: a+b, single.values(), 0)

    for elt in single.values():
        total-=elt
        result+=elt*total
    
    return result

print main()
