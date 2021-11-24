# bfs 
import sys
from collections import deque
input = sys.stdin.readline

# '-' 는 가로로 같은 행에 있으면 1개로 친다
# '|' 는 세로로 같은 열에 있으면 1개로 친다

def sol(i,j,t):
    queue = deque()
    queue.append((i,j,t))
    while queue:
        x,y,T = queue.popleft()
        if visited[x][y] == 1:
            continue
        visited[x][y] = 1
        if T == '-':
            # '-' 같은 행에 연속해서 몇개 있는지 탐색
            if y+1 < m and room[x][y+1] == '-':
                queue.append((x,y+1,T))
        elif T == '|':
            # '|' 같은 열에 연속해서 몇개 있는지 탐색
            if x+1 < n and room[x+1][y] == '|':
                queue.append((x+1,y,T))
    return 1

n, m = map(int, input().split())
room = [input().rstrip() for _ in range(n)]
visited = [[0]*(m) for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            cnt += sol(i,j,room[i][j])
print(cnt)