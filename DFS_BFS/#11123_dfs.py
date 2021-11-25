# dfs
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(x,y):
    
    world[x][y] = '.'
    # for i in range(4):
    #     X = x + dir[i][0]
    #     Y = y + dir[i][1]
    #     if 0 <= X < R and 0 <= Y < C and world[X][Y] == '#':
    #         dfs(X,Y)
    # 위 방식보다 아래 방식이 훨씬 빠르다.
    if x-1 >= 0 and world[x-1][y] == '#':
        dfs(x-1, y)
    if x+1 < R and world[x+1][y] == '#':
        dfs(x+1, y)
    if y-1 >= 0 and world[x][y-1] == '#':
        dfs(x, y-1)
    if y+1 < C and world[x][y+1] == '#':
        dfs(x, y+1)
    return 1

dir = [(1,0),(-1,0),(0,1),(0,-1)]
for _ in range(int(input())):
    R ,C = map(int, input().split())     
    cnt = 0
    world = [list(input().rstrip()) for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if world[i][j] == '#':
                cnt += dfs(i,j)
    print(cnt)