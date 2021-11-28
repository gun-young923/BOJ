# =============================================================
# bfs python3 -> 3636ms // pypy3 -> 1000ms
import sys
from collections import deque
from itertools import combinations
from copy import deepcopy
input = sys.stdin.readline

lab = []
empty_ = []
n, m = map(int, input().split())
for i in range(n):
    line = list(map(int, input().split()))
    lab.append(line)
    for j in range(m):
        if line[j] == 0:
            empty_.append((i,j))

def bfs(x,y,labs):
    v[x][y] = 1
    arr = []
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        arr.append(labs[x][y])
        if 0 <= x-1 and v[x-1][y] == 0 and labs[x-1][y] != 1:
            q.append((x-1,y))
            v[x-1][y] = 1
        if x+1 < n and v[x+1][y] == 0 and labs[x+1][y] != 1:
            q.append((x+1,y))
            v[x+1][y] = 1
        if 0 <= y-1 and v[x][y-1] == 0 and labs[x][y-1] != 1:
            q.append((x,y-1))
            v[x][y-1] = 1
        if y+1 < m and v[x][y+1] == 0 and labs[x][y+1] != 1:
            q.append((x,y+1))
            v[x][y+1] = 1
    return arr
  
def sol(c):
    labs = deepcopy(lab)
    arr_ = []
    cnt = 0
    for i,j in c:
        labs[i][j] = 1
    for i in range(n):
        for j in range(m):
            if v[i][j] == 0 and labs[i][j] != 1:
                arr_ = bfs(i,j,labs)
                if 2 not in arr_:
                    cnt += len(arr_)
    return cnt

if __name__ == '__main__':
    max_val = 0
    candidates = list(combinations(empty_,3))
    for i in candidates:
        v = [[0]*m for _ in range(n)]
        ans = sol(list(i))
        max_val = max(max_val, ans)
    print(max_val)