def main(l):
    res=0
    for elt in l:
        res^=elt
    return res
        
    

l=[1,2,3,4,5,1,2,3,4]
l=[8,2,2,2,2]
print main(l)
