""" import sys
from collections import deque
input = sys.stdin.readline

n,l,s = map(int, input().split())
line = []
arr = [[0]*(n+1) for _ in range(n+1)]
for i in range(l):
    a,b = map(int, input().split())
    arr[a][b] = arr[b][a] = 1

def dfs(current_node, row, foot_print):
    foot_print += [current_node]
    for search_node in range(len(row[current_node])):
        if row[current_node][search_node] and search_node not in foot_print:
            foot_print = dfs(search_node, row, foot_print)
    return foot_print

def bfs(start):
    queue = deque([start])
    footprint = [start]
    while queue:
        current_node = queue.popleft()
        for search_node in range(len(arr[current_node])):
            if arr[current_node][search_node] and search_node not in footprint:
                footprint += [search_node]
                queue.append(search_node)
    return footprint
    

print(dfs(s,arr,[]))
print(bfs(s)) """



import sys
from collections import deque
input = sys.stdin.readline

n,m,v = map(int, input().split())
line = []
arr = [[0]*(n+1) for _ in range(n+1)]
for i in range(l):
    a,b = map(int, input().split())
    arr[a][b] = arr[b][a] = 1


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