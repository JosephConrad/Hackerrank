def solve( x, y, pacman_x, pacman_y, food_x, food_y, grid):
    visited=set()
    stack=[]
    nodes=[]
    dfs(x,y):
        if grid[x][y]=="%" or (x,y) in visited: return 0
        stack.append((x,y))
        visited.add((x,y))
        nodes.add((x,y)) 
        if grid[x][y]==".": return 1
        if dfs(x+1, y): return 1
        if dfs(x, y+1): return 1
        if dfs(x, y-1): return 1
        if dfs(x-1, y): return 1
        stack.pop()
        return 0
    
    dfs(pacman_x, pacman_y)






pacman_r, pacman_c = [ int(i) for i in raw_input().strip().split() ]
food_r, food_c = [ int(i) for i in raw_input().strip().split() ]
r,c = [ int(i) for i in raw_input().strip().split() ]

grid = []
for i in xrange(0, r):
    grid.append(raw_input().strip())

solve(r, c, pacman_r, pacman_c, food_r, food_c, grid)
