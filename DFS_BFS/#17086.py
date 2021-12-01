"""
문제
N×M 크기의 공간에 아기 상어 여러 마리가 있다. 공간은 1×1 크기의 정사각형 칸으로 나누어져 있다. 
한 칸에는 아기 상어가 최대 1마리 존재한다.

어떤 칸의 안전 거리는 그 칸과 가장 거리가 가까운 아기 상어와의 거리이다. 
두 칸의 거리는 하나의 칸에서 다른 칸으로 가기 위해서 지나야 하는 칸의 수이고, 이동은 인접한 8방향(대각선 포함)이 가능하다.

안전 거리가 가장 큰 칸을 구해보자. 

입력
첫째 줄에 공간의 크기 N과 M(2 ≤ N, M ≤ 50)이 주어진다. 
둘째 줄부터 N개의 줄에 공간의 상태가 주어지며, 0은 빈 칸, 1은 아기 상어가 있는 칸이다. 빈 칸의 개수가 한 개 이상인 입력만 주어진다.

출력
첫째 줄에 안전 거리의 최댓값을 출력한다.

예제 입력 1     예제 출력 1 
5 4             2
0 0 1 0
0 0 0 0
1 0 0 0
0 0 0 0
0 0 0 1


예제 입력 2     예제 출력 2 
7 4             2
0 0 0 1
0 1 0 0
0 0 0 0
0 0 0 1
0 0 0 0
0 1 0 0
0 0 0 1


"""

import sys
from collections import deque
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def bfs(x,y,cnt):
    vis = [[0]*m for _ in range(n)]
    ans = []
    vis[x][y] = 1
    queue = deque()
    queue.append((x,y,cnt))
    while queue:
        x,y,cnt = queue.popleft()
        if cnt != -1 and (x,y) in temp:
            ans.append(cnt)
            continue
        cnt += 1
        for i in range(8):
            X = x + dir[i][0]
            Y = y + dir[i][1]
            if 0 <= X < n and 0 <= Y < m and vis[X][Y]==0:
                queue.append((X,Y,cnt))
                vis[X][Y] = 1
    print(ans)
    return min(ans)

arr = []
temp = []
dir = [(1,0),(1,1),(1,-1),(-1,0),(-1,1),(-1,-1),(0,1),(0,-1)]
n,m = map(int,input().split())
for i in range(n):
    line = list(map(int, input().split()))
    arr.append(line)
    for j in range(m):
        if line[j] == 1:
            temp.append((i,j))

max_val = 0
for x,y in temp:
    max_val = max(max_val,bfs(x,y,-1))
print(max_val)

# 출발은 임의의 칸/ 마지막 상어칸 포함한 거리 
# (0 0 0 0 1) 인경우 첫 0 부터 1까지 거리는 4
