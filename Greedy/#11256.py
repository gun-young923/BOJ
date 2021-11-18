import sys
input = sys.stdin.readline

case = int(input())
for _ in range(case):
    arr=[]
    box=0
    num , n = map(int, input().split())
    for i in range(n):
        a,b = map(int, input().split())
        arr.append(a*b)
    arr.sort()
    for i in range(n):
        box += arr.pop()
        if box >= num:
            box = i+1
            break
    print(box)