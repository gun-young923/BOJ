def dfs(x, y, word):
    if len(word) == 6: 
        if word not in ans: 
            ans.append(word)
        return
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1] 
    for k in range(4):
        X = x + dx[k]
        Y = y + dy[k]
        if 0 <= X < 5 and 0 <= Y < 5:
            dfs(X, Y, word + g[X][Y]) 
g = [list(map(str, input().split())) for _ in range(5)]
ans = []
for i in range(5):
    for j in range(5):
        dfs(i, j, g[i][j]) 
print(len(ans))
