import sys

input = sys.stdin.readline
n,k = map(int, input().split()) # n = 햄버거 갯수 , k = 거리
arr = input().rstrip()
stand=[]
ans=[0]*n
for i in range(n):
    if arr[i]=='P':
        stand.append(i)
for i in range(len(stand)):
    for j in range(-k,k+1):
        if j==0 or stand[i]+j<0 or stand[i]+j>=n:continue
        if arr[stand[i]+j]=='H':
            if ans[stand[i]+j]!=1:
                ans[stand[i]+j]=1
                break
print(sum(ans))