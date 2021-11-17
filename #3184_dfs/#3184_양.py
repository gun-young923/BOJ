import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(x,y):
    visited[x][y] = 1
    if world[x][y] == 'o':      # sheep
        cnt[0] += 1
    elif world[x][y] == 'v':    # wolf 
        cnt[1] += 1
    for i in range(4):
        X = x + dir[i][0]
        Y = y + dir[i][1]
        if 0 <= X < R and 0 <= Y < C and visited[X][Y]==0 and world[X][Y] != '#':
            dfs(X,Y)
    return cnt

R ,C = map(int, input().split())                # input R, C
world = []
visited = [[0]*C for _ in range(R)]
dir = [(1,0),(-1,0),(0,1),(0,-1)]
ans = [0,0]
for i in range(R):              
    world.append(list(input().rstrip()))        # input world

for i in range(R):
    for j in range(C):
        if visited[i][j] == 0 and world[i][j] != '#':
            cnt = [0,0]
            sheep, wolf = dfs(i,j)
            # print(sheep , wolf, '\n--------------------') # check
            if sheep > wolf:
                ans[0] += sheep
            else :
                ans[1] += wolf
print(ans[0],ans[1])

# 2 
"""
양과 늑대의 좌표만 각각 저장 -> 그 좌표들만 저격하여 dfs()돌린다 (필요없는부분 투자 X)
    지나간 부분은 #으로 변경 -> visited[] 만들필요 X
"""
