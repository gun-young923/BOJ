# dfm방식 재귀
import sys
sys.setrecursionlimit(100000) #재귀함수 깊이 제한 수정
input = sys.stdin.readline

n = int(input())
g = [list(input().rstrip()) for _ in range(n)]
ans = []
dir = [(-1,0),(1,0),(0,-1),(0,1)]

def dfs(x,y,color):
    if x < 0 or x > n-1 or y < 0 or y > n-1:
        return False
    if g[x][y] == color:
        if color == 'R' or color == 'G':
            g[x][y] = 'RG'
        else:
            g[x][y] = 'V'
        for i in range(4):
            X = x+dir[i][0]
            Y = y+dir[i][1]
            dfs(X,Y,color)
        return True
    else:
        return False
        
Colors = ['R','G','B','RG']
for i in Colors:
    cnt = 0
    for x in range(n):
        for y in range(n):
            if dfs(x,y,i) == True:
                cnt += 1
    ans.append(cnt)

print(sum(ans[:3]),sum(ans[2:]))