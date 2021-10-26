import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort(reverse=True)
ans=0
for i in range(n):
    if arr[i]*(i+1) > ans:
        ans = arr[i]*(i+1)
print(ans)
