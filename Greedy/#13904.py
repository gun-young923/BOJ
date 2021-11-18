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
    

#1
""" import sys

def f_max(s):
    cnt=[0,0]
    for i in range(len(s)):
        if s[i][1] > cnt[1]:
            cnt=s[i]
    return cnt

def f_day(s,x):
    a=[]
    for i in range(len(s)):
        if s[i][0] >= x:
            a.append(s[i])
    return a

input = sys.stdin.readline
arr = [list(map(int, input().split())) for i in range(int(input()))]
n = max(arr)[0]
ans = [0]*n
for i in range(n):
    arr_1 = f_day(arr, n-i)
    ans[n-i-1] = (f_max(arr_1)[1])
    if arr_1==[]:
        continue
    arr.remove(f_max(arr_1))
print(sum(ans)) """