# bfs 'o' , 'v' 를 '#'로 변환하여 진행
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y):
    cnt[0] = 1 if world[x][y] == 'o' else 0
    cnt[1] = 1 if world[x][y] == 'v' else 0
    world[x][y] = '#'
    queue = deque()
    queue.append([x,y]) 
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            X = x + dir[i][0]
            Y = y + dir[i][1]
            if 0 <= X < R and 0 <= Y < C and world[X][Y] != '#': 
                if world[X][Y] == 'o':
                    cnt[0] += 1
                elif world[X][Y] == 'v':
                    cnt[1] += 1
                world[X][Y] = '#'  
                queue.append([X,Y])
    return cnt

R ,C = map(int, input().split())        # input R, C
world = []
s_w = []
dir = [(1,0),(-1,0),(0,1),(0,-1)]
ans = [0,0]
for i in range(R):              
    temp = list(input().rstrip())       # input world
    world.append(temp)
    for j in range(len(temp)):
        if temp[j] == 'o' or temp[j] == 'v':
            s_w.append([i,j])
for i in (s_w):
    x,y = i
    if world[x][y] != '#':      #======= #으로 바꿔보자
        cnt = [0,0]
        sheep , wolf = bfs(x,y)
        if sheep > wolf:
            ans[0] += sheep
        else :
            ans[1] += wolf
print(ans[0],ans[1])

# bfs visited[] 사용
""" import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y):
    visited[x][y] = 1
    queue = deque()
    queue.append([x,y]) 
    while queue:
        x,y = queue.popleft()
        if world[x][y] == 'o':
            cnt[0] += 1
        elif world[x][y] == 'v':
            cnt[1] += 1
        for i in range(4):
            X = x + dir[i][0]
            Y = y + dir[i][1]
            if 0 <= X < R and 0 <= Y < C and visited[X][Y] == 0:
                visited[X][Y] = 1
                if world[X][Y] != '#':
                    queue.append([X,Y])
    return cnt

R ,C = map(int, input().split())       
world = []
s_w = []
visited = [[0]*C for _ in range(R)]
dir = [(1,0),(-1,0),(0,1),(0,-1)]
ans = [0,0]

for i in range(R):              
    temp = list(input().rstrip())       
    world.append(temp)
    for j in range(len(temp)):
        if temp[j] == 'o' or temp[j] == 'v':
            s_w.append([i,j])       
for i in (s_w):
    x,y = i
    if visited[x][y] == 0:      
        cnt = [0,0]
        sheep , wolf = bfs(x,y)
        if sheep > wolf:
            ans[0] += sheep
        else :
            ans[1] += wolf
print(ans[0],ans[1]) """