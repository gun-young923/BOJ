import sys

input = sys.stdin.readline
n = int(input().rstrip())
arr = [list(map(int, input().split())) for i in range(n)]
arr.sort(key = lambda x : -x[1])
ans=[0]*max(arr)[0]

for i in range(n):
    j=0
    if ans[arr[i][0]-1]==0:
        ans[arr[i][0]-1] = arr[i][1]
    else:
        while(arr[i][0]-1-j>0):
            if ans[arr[i][0]-1-j]==0:
                break
            j+=1
        if ans[arr[i][0]-1-j]==0:
            ans[arr[i][0]-1-j] = arr[i][1]
print(sum(ans))
    
