import sys
input = sys.stdin.readline
arr = [[0,0,0],[0,0,0]]
for i in range(3):
    a,b = map(int, input().split())
    arr[0][i] = a
    arr[1][i] = b
ans = []
for i in range(2):
    cnt = 3
    num = 0
    for j in arr[i]:
        if cnt > arr[i].count(j):
            cnt = arr[i].count(j)
            num = j
    ans.append(str(num))
print(' '.join(ans))