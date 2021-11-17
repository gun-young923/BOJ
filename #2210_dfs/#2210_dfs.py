
import sys
input = sys.stdin.readline



def dfs(x,y,word):
    if x < 0 or x > 4 or y < 0 or y > 4:
        return
    if len(word) == 6:
        if word not in 
        pass

    # arr.append(g[x][y])
    for i in range(4):
        X = x + dir[i][0]
        Y = y + dir[i][1]
        dfs(X,Y)


ans = []
g = []
dir = [(-1,0),(1,0),(0,-1),(0,1)]
for i in range(5):
    g.append(list(map(int, input().split())))

for i in range(5):
    for j in range(5):
        
        dfs(i,j,g[i][j])
