# dfs
# pypy3로 했을때 통과 python3는 시간초과
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(x,y,dir,num):
    global cnt
    if n < 5:
        return 
    elif n == 5:
        cnt = 2
        return 
    if arr[x][y] != 0:
        if num == n:
            cnt += 1
        return 
    arr[x][y] = num + 1
    if arr[x][y] == n + 1:
        arr[x][y] = 0
        return
    for i in range(2):
        X = x + d[dir][i][0]
        Y = y + d[dir][i][1]
        if 0 <= X < 55 and 0 <= Y < 55 :
            dfs(X,Y,d[dir][i][2],arr[x][y])
    arr[x][y] = 0
    return
    
n = int(input())
cnt = 0
arr = [[0]*55 for _ in range(55)]
d = [((-1,-1,5),(-1,1,1)),((-1,0,0),(1,1,2)),((-1,1,1),(1,0,3)),
((1,-1,4),(1,1,2)),((-1,-1,5),(1,0,3)),((1,-1,4),(-1,0,0))]
arr[26][25] = 30
dfs(25,25,0,0)
print(cnt)