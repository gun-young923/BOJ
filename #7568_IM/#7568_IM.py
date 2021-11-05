import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
for i in arr :
    ans = 1
    for j in arr :
        if i[0] < j[0] and i[1] < j[1]:
                ans += 1
    print(ans,end=' ')
