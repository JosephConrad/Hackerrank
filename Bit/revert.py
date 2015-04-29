


def revert(n):
    pom=0
    while n!=0:
        pom<<=1
        pom|=(n&1)
        n>>=1
    return pom

print revert(6)
