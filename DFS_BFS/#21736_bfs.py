# bfs 로 풀기

# dfs visited[] 사용
import sys
from collections import deque
input =sys.stdin.readline

def bfs(s):
    global cnt
    x,y = s
    visited[x][y] = 1 
    queue = deque()
    queue.append(s)
    while queue:
        x,y = queue.popleft()
        if cmap[x][y] == 'P':
            cnt += 1
        for i in range(4):
            X = x + dir[i][0]
            Y = y + dir[i][1]
            if 0 <= X < n and 0 <= Y < m and visited[X][Y] == 0 and cmap[X][Y] != 'X':
                queue.append((X,Y))
                visited[X][Y] = 1
    return cnt
cmap = []
cnt = 0
dir = [(-1,0),(1,0),(0,-1),(0,1)]
n, m = map(int, input().split())
visited = [[0]*m for _ in range(n)]
for i in range(n):
    info = list(input().rstrip())
    if 'I' in info:
        start = (i,info.index('I'))
    cmap.append(info)
ans = bfs(start)
print(ans if ans != 0 else 'TT')

# 지나간 곳 'X'로 교체
""" import sys
sys.setrecursionlimit(1000000)
input =sys.stdin.readline

def dfs(x,y):       
    global cnt 
    for i in range(4):
        X = x + dir[i][0]
        Y = y + dir[i][1]
        if 0 <= X < n and 0 <= Y < m and cmap[X][Y] != 'X':
            if cmap[X][Y] == 'P':
                cnt += 1        
            cmap[X][Y] = 'X'
            dfs(X,Y)
    return cnt
cmap = []
cnt = 0
dir = [(-1,0),(1,0),(0,-1),(0,1)]
n, m = map(int, input().split())
for i in range(n):
    info = list(input().rstrip())
    if 'I' in info:
        I = info.index('I')
        start = (i,I)
        info[I] = 'X'
    cmap.append(info)
ans = dfs(start[0],start[1])
print(ans if ans != 0 else 'TT') """