def printf(n, grid):
    for g in grid:
        print '\t'.join(map(lambda x: str(x), g))


def process(n, grid):
    print n
    printf(n, grid)



def main():
    for i in range(input()):
        n = int(input())
        l1 = list(map(lambda x: int(x), raw_input()))
        l2 = list(map(lambda x: int(x), raw_input()))
        process(n, [l1,l2])

main()
