# bfs 방식 -> 재귀X
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
g = [list(input().rstrip()) for _ in range(n)]
ans = [0,0]
dir = [(-1,0),(1,0),(0,-1),(0,1)]
queue = deque()

def bfs(i,j):
    color = g[i][j]
    visited[i][j] = 1
    queue.append((i,j))
    while queue:
        x,y = queue.popleft()
        for a in range(4):
            X = x+dir[a][0]
            Y = y+dir[a][1]
            if X < 0 or X > n-1 or Y < 0 or Y > n-1:
                continue
            if g[X][Y] == color and visited[X][Y] == 0:
                visited[X][Y] = 1
                queue.append((X,Y))
    return 1

def RtoG():                     # 'R' 을 'G'로 변환
    for i in range(n):
        for j in range(n):
            if g[i][j] == 'R':
                g[i][j] = 'G'

visited = [[0]*n for _ in range(n)]
for i in range(n):              # 적록색약이 아닌경우
    for j in range(n):
        if visited[i][j] == 1:
            continue
        else:
            ans[0] += bfs(i,j)
visited = [[0]*n for _ in range(n)]
for i in range(n):              # 적록색약인 경우
    for j in range(n):
        if visited[i][j] == 1:
            continue
        else:
            RtoG()
            ans[1] += bfs(i,j)
# print(' '.join(list(map(str, ans))))
print(ans[0],ans[1])