import sys

t = int(sys.stdin.readline())
for i in range(t): 
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))

    arr.sort()
    s = max(arr[1]-arr[0], arr[n-1]-arr[n-2])
    for i in range(n-2): 
        if arr[i+2]-arr[i]>s:
            s = arr[i+2]-arr[i]
    print(s)

#1
""" import sys

t = int(sys.stdin.readline())
for i in range(t): 
    a,b=[],[]
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()
    for i in range(n): 
        if i==0 or i%2==0:
            a.append(arr[i])
        else:
            b.append(arr[i])
    b.reverse()
    a = a + b
    s = abs(a[n-1]-a[0])
    for i in range(n-1):
        if abs(a[i+1] - a[i]) > s:
            s = abs(a[i+1] - a[i])
    print(s) """



