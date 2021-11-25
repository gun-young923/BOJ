# bfs 1
""" import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y):
    visited[x][y] = 1
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()

        if g[x][y] == 'k':
            cnt[0] += 1
        elif g[x][y] == 'v':
            cnt[1] += 1
        for i in range(4):
            X = x + dir[i][0]
            Y = y + dir[i][1]
            if 0 <= X < r and 0 <= Y < c and visited[X][Y] == 0 and g[X][Y] != '#':
                visited[X][Y] = 1
                queue.append((X,Y))

    return

r, c = map(int, input().split())
dir = [(1,0),(-1,0),(0,1),(0,-1)]
spot, g = [],[]
visited = [[0]*c for _ in range(r)]
ans = [0,0]
for i in range(r):
    line = input().rstrip()
    g.append(line)
    for j in range(c):
        if line[j] == 'v' or line[j] == 'k':
            spot.append((i,j))

for i in spot:
    x,y = i
    if visited[x][y] == 0:
        cnt = [0,0]
        bfs(x,y)
        if cnt[0] > cnt[1]:
            ans[0] += cnt[0]
        else :
            ans[1] += cnt[1]
print(ans[0], ans[1]) """

# bfs 2 -> '#'으로 변경
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y):
    V, K = 0,0
    if g[x][y] == 'k':
        K += 1
    elif g[x][y] == 'v':
        V += 1
    g[x][y] = '#'
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            X = x + dir[i][0]
            Y = y + dir[i][1]
            if 0 <= X < r and 0 <= Y < c and g[X][Y] != '#':
                q.append((X,Y))
                if g[X][Y] == 'k':
                    K += 1
                elif g[X][Y] == 'v':
                    V += 1
                g[X][Y] = '#'
    return K,V

r, c = map(int, input().split())
dir = [(1,0),(-1,0),(0,1),(0,-1)]
g = []

ans = [0,0]
g = [list(input().rstrip()) for _ in range(r)]

for i in range(r):
    for j in range(c):
        
        if g[i][j] != '#':
            K, V = bfs(i,j)
            if K > V:
                ans[0] += K
            else :
                ans[1] += V                
print(ans[0], ans[1])