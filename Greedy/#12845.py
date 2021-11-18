import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
print(max(arr)*(n-1) + sum(sorted(arr)[:-1]))