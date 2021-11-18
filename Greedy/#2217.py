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


#2
""" import sys
In = sys.stdin.readline

def main():
    n = int(In())
    rope = [0] * 10001
    for _ in range(n):
        rope[int(In())] += 1
    m, s = 0, 0
    for x in range(10000,-1,-1):
        s += rope[x]
        m = max(m, x * s)
    print(m)
main() """