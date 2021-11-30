# bfs -------------------------------------------------
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y):
    g[x][y] = 0
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        for i in range(8):
            X = x + d[i][0]
            Y = y + d[i][1]
            if 0 <= X < n and 0 <= Y < m and g[X][Y] == 1:
                queue.append((X,Y))
                g[X][Y] = 0 
    return 1

n, m = map(int, input().split())
arr = []
g = []
d = [(-1,0),(1,0),(1,1),(-1,-1),(0,1),(0,-1),(1,-1),(-1,1)]
ans = 0
for i in range(n):
    line = list(map(int,input().split()))
    g.append(line)
    for j in range(m):
        if line[j] == 1:
            arr.append((i,j))

for x,y in arr:
    if g[x][y] == 1:
        ans += bfs(x,y)
print(ans)