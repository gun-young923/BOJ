import sys
from collections import deque
input = sys.stdin.readline

n,m,v = map(int, input().split())
g = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b = map(int, input().split())
    g[a][b] = g[b][a] = 1
def dfs(v):
    visited[v]=True
    print(v,end=' ')
    for i in range(1,n+1):
        if not visited[i] and g[v][i]==1:
            dfs(i)
def bfs(v):
    queue = deque([v])
    visited[v] = True

    while queue:
        v = queue.popleft()
        print(v,end=' ')

        for i in range(1,n+1):
            if not visited[i] and g[v][i]==1:
                queue.append(i)
                visited[i]=True
visited = [False]*(n+1)
dfs(v)
print()
visited = [False]*(n+1)
bfs(v)