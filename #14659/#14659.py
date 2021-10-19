#기준점에서 보다 낮은곳까지 탐색후 기준점 보다 높은곳 발견 시 
# 그 사이의 낮은 봉우리는 어짜피 지금 걸린 높은곳에 걸리기 때문에 
# 걸린 높은곳에서 다시 낮은곳을 찾는다.
import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

cnt=0
ans = 0
std = 0
for i in arr:
    if i < std:
        cnt += 1
    else:
        std = i
        cnt = 0
    ans = max(ans, cnt)
print(ans)

#1
""" import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

cnt=[0]*n
for i in range(n-1):
    for j in range(i+1,n):
        if arr[i] > arr[j]:
            cnt[i]+=1
        else:
            break
print(max(cnt)) """