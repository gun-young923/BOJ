import sys
input = sys.stdin.readline

n = int(input())
arr = sorted([list(map(int,input().split())) for _ in range(n)])
ans = arr[0][1] - arr[0][0]
std = arr[0][1]
for i in arr[1:]:
    if i[0] < std and i[1] > std:
        ans += i[1] - std
        std = i[1]
    elif i[0] >= std and i[1] > std:
        ans += i[1]-i[0]
        std = i[1]
print(ans)