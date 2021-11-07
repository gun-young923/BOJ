import sys
input = sys.stdin.readline
ans, cnt = 0, 0
for i in range(4):
    down , up = map(int, input().split())
    cnt = cnt + up - down
    if cnt > ans:
        ans = cnt
print(ans)
    