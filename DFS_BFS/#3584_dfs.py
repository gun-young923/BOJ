# dfs 재귀  visited[]
        
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def dfs(i):
    if visited[i] == 1:
        print(i)
        # ans.append(str(i))
        return
    visited[i] = 1
    if graph[i] == 0:
        return
    dfs(graph[i])
    return

ans = []
t = int(input())
for _ in range(t):
    n = int(input())
    graph = [0]*(n+1)
    for i in range(n-1):
        parent, child = map(int, input().split())
        graph[child] = parent
    c1, c2 = map(int, input().split())    # 여기까지 입력     
    visited = [0]*(n+1)
    for i in (c1,c2):
        dfs(i)
# print(' '.join(ans))