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


