# pypy3 520ms / python3 시간초과
# 각각의 0마다 가장가까운 1까지 bfs로 탐색 후 그중 가장 큰값
""" import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y,cnt):
    vis = [[0]*m for _ in range(n)]
    vis[x][y] = 1
    queue = deque()
    queue.append((x,y,cnt))
    while queue:
        x,y,cnt = queue.popleft()
        cnt += 1
        if cnt == 0 and arr[x][y] == 1:     # 1 시작인 경우 안전거리 0
            return 0
        if arr[x][y] == 1:
            return cnt
        for i in range(8):
            X = x + dir[i][0]
            Y = y + dir[i][1]
            if 0 <= X < n and 0 <= Y < m and vis[X][Y]==0:
                queue.append((X,Y,cnt))
                vis[X][Y] = 1

arr = []
temp = []
dir = [(1,0),(1,1),(1,-1),(-1,0),(-1,1),(-1,-1),(0,1),(0,-1)]
n,m = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(n)]       #input
ans = []
for i in range(n):
    for j in range(m):
        ans.append(bfs(i,j,-1))
print(max(ans)) """

# 1의 위치 찾아서 1부터 0으로 count 하며 뻗어나가며 0 에서 가장 가까운 1까지의 거리 표기
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y,cnt):
    ans = 0
    queue = deque()
    queue.extend(temp)
    while queue:
        x,y,cnt = queue.popleft()
        ans = max(ans,cnt)
        for i in range(8):
            X = x + dir[i][0]
            Y = y + dir[i][1]
            if 0 <= X < n and 0 <= Y < m and arr[X][Y]==0:
                queue.append((X,Y,cnt+1))
                arr[X][Y] = cnt + 1
    return ans

n, m=map(int, input().split())
temp = []
arr = []
dir = [(1,0),(1,1),(1,-1),(-1,0),(-1,1),(-1,-1),(0,1),(0,-1)]
for i in range(n):                              
    line = list(map(int, input().split()))
    arr.append(line)
    for j in range(m):
        if line[j] == 1:
            temp.append((i,j,0))
print(bfs(0,0,0))
