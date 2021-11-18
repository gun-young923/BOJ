import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
print(arr.pop(arr.index(max(arr))) + sum(arr)/2)