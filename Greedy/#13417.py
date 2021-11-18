import sys

input = sys.stdin.readline
for i in range(int(input())):
    s = []
    n = int(input())
    arr = list(map(str, input().split()))
    s.append(arr[0])
    for i in range(1,n):
        if arr[i] > s[0]:
            s.append(arr[i])
        else :
            s.insert(0, arr[i])
    print("".join(s))
