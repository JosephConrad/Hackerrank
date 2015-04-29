def solve( x, y, pacman_x, pacman_y, food_x, food_y, grid):
    q=[(pacman_x, pacman_y, 0)]
    nodes=[]
    visited=set()
    parent={}
    path=[(x,y)]
    def bfs(x,y):
        while q!=[]:
            (x,y,step)=q.pop(0)
            if grid[x][y]=="%" or (x,y) in visited: continue
            visited.add((x,y))
            nodes.append((x,y)) 
            if len(path)-1<step: path.append((x,y))
            else:
                path[step]=(x,y)
            if grid[x][y]==".": return 1
            step+=1
            q.append((x-1, y, step))
            parent[]
            q.append((x, y-1, step))
            q.append((x, y+1, step))
            q.append((x+1, y, step))
    
    bfs(pacman_x, pacman_y)
    print len(nodes)
    for pos in nodes:
        print str(pos[0]), str(pos[1])
    print len(path) - 1
    for pos in path:
        print str(pos[0]), str(pos[1])





pacman_r, pacman_c = [ int(i) for i in raw_input().strip().split() ]
food_r, food_c = [ int(i) for i in raw_input().strip().split() ]
r,c = [ int(i) for i in raw_input().strip().split() ]

grid = []
for i in xrange(0, r):
    grid.append(raw_input().strip())

solve(r, c, pacman_r, pacman_c, food_r, food_c, grid)
