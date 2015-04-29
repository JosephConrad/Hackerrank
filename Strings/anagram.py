

def process(word):
    size=len(word)
    if size%2==1: return -1
    w1=word[:size/2]
    w2=word[size/2:]
    
    d=dict()
    for elt in w1:
        d[elt] = d[elt]+1 if elt in d else 1
    for elt in w2:
        d[elt] = d[elt]-1 if elt in d else -1
    res=0
    for key, value in d.iteritems():
       res+=abs(value) 
    return  res/2

def main():
    for i in xrange(input()):
        word=str(raw_input())    
        print process(word)


main()
