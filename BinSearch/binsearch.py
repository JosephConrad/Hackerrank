


def binSearch(seq, elt):
    l=0
    r=len(seq)-1
    while l<r:
        m=(l+r)/2+1
        if seq[m]>elt:
            r=m-1
        else:
            l=m
    return l 







print binSearch([4,5], 4)
