import sys
input = sys.stdin.readline

arr=sorted([int(input()) for _ in range(int(input()))], reverse=True)

for i in range(len(arr)):
    if (i+1)%3==0:
        arr[i]=0
print(sum(arr))
    