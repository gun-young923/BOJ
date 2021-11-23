# bfs // visited[]
import sys
from collections import deque
input = sys.stdin.readline

def bfs(s):                 # queue에 append시 중복 방지 / 아래보다 계산 수 약간 적음
    queue = deque()
    queue.append(s)
    visited[s] = 1
    while queue:
        s = queue.popleft()
        for i in (1,-1):
            S = s + i*arr[s]
            if 0 <= S < n and visited[S] == 0:
                queue.append(S)
                visited[S] = 1 
    return

# 위와 같은 함수. 방식만 약간 다름 
""" def bfs(s):             # 위보다 계산 수 약간 많음 (queue안에 중복)
    queue = deque()
    queue.append(s)
    while queue:
        s = queue.popleft()
        print('--- %d ---'%(s))
        visited[s] = 1
        for i in (1,-1):
            S = s + i*arr[s]
            if 0 <= S < n and visited[S] == 0:
                queue.append(S)
    return """
    
n = int(input())
arr = list(map(int, input().split())) 
s = int(input())
visited = [0]*(n)
bfs(s-1)
print(visited.count(1))
