import sys

n = int(sys.stdin.readline())
w = list(map(int, sys.stdin.readline().split()))
w.sort()
cnt = 0
for i in range(n):
    if cnt+1 >= w[i]:
        cnt += w[i]
    else:
        break
print(cnt+1)