# bfs
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y):
    q = deque()
    q.append((x,y))
    world[x][y] = '.'
    while q:
        x,y = q.popleft()
        if x-1 >= 0 and world[x-1][y] == '#':
            q.append((x-1,y))
            world[x-1][y] = '.'
        if x+1 < R and world[x+1][y] == '#':
            q.append((x+1,y))
            world[x+1][y] = '.'
        if y-1 >= 0 and world[x][y-1] == '#':
            q.append((x,y-1))
            world[x][y-1] = '.'
        if y+1 < C and world[x][y+1] == '#':
            q.append((x,y+1))
            world[x][y+1] = '.'
    return 1

for _ in range(int(input())):
    R ,C = map(int, input().split())
    dir = [(1,0),(-1,0),(0,1),(0,-1)]
    ans = 0
    world = [list(input().rstrip()) for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if world[i][j] == '#':
                ans += bfs(i,j)
    print(ans)