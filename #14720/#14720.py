#순서 딸 초 바 딸 -> (0 1 2 0)

import sys
input = sys.stdin.readline
num ,cnt= 0,0
n = int(input())
arr = list(map(int, input().split()))
for i in arr:
    if i == num:
        num += 1
        if num == 3:
            num = 0
        cnt += 1
print(cnt)