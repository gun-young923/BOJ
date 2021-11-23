# dfs // visited[]
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(s):
    if visited[s] == 1:
        return
    visited[s] = 1
    S1 = s + arr[s] 
    S2 = s - arr[s]
    if S1 < n and visited[S1] == 0:
        dfs(S1)
    if S2 >= 0 and visited[S2] == 0:
        dfs(S2) 
    return

n = int(input())
arr = list(map(int, input().split())) 
s = int(input())
visited = [0]*(n)
dfs(s-1)
print(visited.count(1))