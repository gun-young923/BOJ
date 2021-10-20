import sys
input = sys.stdin.readline

arr=[]
a,b = map(int, input().split())
n = int(input())
for i in range(n):
    arr.append(int(input()))

cnt=1000
for i in arr:
    if cnt > abs(b-i)+1:
        cnt = abs(b-i)+1
if cnt > abs(a-b):
    print(abs(a-b))
else:
    print(cnt)
