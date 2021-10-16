import sys
input = sys.stdin.readline

n,m = map(int, input().split())
left , right , cnt = 1, m , 0
j = int(input())
arr = [int(input()) for _ in range(j)]
for i in arr:
    if i < left:
        cnt += left - i
        right -= left - i
        left -= left - i
    elif (i >= left) and (i <= right):
        continue
    else:
        cnt += i - right
        left += i - right
        right += i - right
print(cnt)