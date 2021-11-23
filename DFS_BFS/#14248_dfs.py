# dfs
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

# flag를 주어 def 안에서 열별로 탐색할지 행별로 탐색할지 결정?
# '-' 는 가로로 같은 행에 있으면 1개로 친다
# '|' 는 세로로 같은 열에 있으면 1개로 친다

def sol(i,j,t):
    visited[i][j] = 1
    if t == '-':
        # '-' 같은 행에 연속해서 몇개 있는지 탐색
        if j+1 < m and room[i][j+1] == '-':
            sol(i,j+1,t)
    elif t == '|':
        # '|' 같은 열에 연속해서 몇개 있는지 탐색
        if i+1 < n and room[i+1][j] == '|':
            sol(i+1,j,t)
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


# bfs
""" import sys
from collections import deque
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

# flag를 주어 def 안에서 열별로 탐색할지 행별로 탐색할지 결정?
# '-' 는 가로로 같은 행에 있으면 1개로 친다
# '|' 는 세로로 같은 열에 있으면 1개로 친다

def sol(i,j,t):
    visited[i][j] = 1
    if t == '-':
        # '-' 같은 행에 연속해서 몇개 있는지 탐색
        if j+1 < m and room[i][j+1] == '-':
            sol(i,j+1,t)
    elif t == '|':
        # '|' 같은 열에 연속해서 몇개 있는지 탐색
        if i+1 < n and room[i+1][j] == '|':
            sol(i+1,j,t)
    return 1

n, m = map(int, input().split())
room = [input().rstrip() for _ in range(n)]
visited = [[0]*(m) for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            cnt += sol(i,j,room[i][j])
print(cnt) """