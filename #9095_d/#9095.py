import sys
input = sys.stdin.readline

def ans(n):
    arr = [1,2,4]
    if n < 4:
        return arr[n-1]
    a,b,c = arr[0],arr[1],arr[2]
    for i in range(4,n+1):
        a,b,c = b,c,a+b+c
    return c

t = int(input())
for i in range(t):
    n = int(input())
    print(ans(n))