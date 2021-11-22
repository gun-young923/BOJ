# bfs
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(8):
            X = x + dir[i][0]
            Y = y + dir[i][1]
            if 0 <= X < m and 0 <= Y < n and visited[X][Y] == 0 and arr[X][Y] == '@':
                visited[X][Y] = 1
                queue.append((X,Y))
    return 1
    
ans = []
while 1:                                # @ == oil deposit / # == nothing
    m, n = map(int, input().split())
    if m == 0:
        break
    oil_d = []
    arr = []
    cnt = 0
    visited = [[0]*n for _ in range(m)]
    dir = [(-1,0),(1,0),(0,-1),(0,1),(1,1),(1,-1),(-1,1),(-1,-1)]

    for i in range(m):
        line = input().rstrip()
        arr.append(line)
        for j in range(n):
            if line[j] == '@':
                oil_d.append((i,j)) # '@'의 좌표 저장
    for i in oil_d:
        x,y = i    
        if visited[x][y] == 0:
            cnt += bfs(x,y)
    ans.append(cnt)
for i in ans:
    print(i)