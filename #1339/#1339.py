import sys
input = sys.stdin.readline
arr=[]
strg=[]
n = int(input())
for i in range(n):
    arr.append(list(input().rstrip()))

for i in range(n):
    for j in range(len(arr[i])):
        flag=0
        for x in strg:
            if arr[i][j] in x:
                x[1] += 10**(len(arr[i])-1-j)
                flag=1
                break
        if flag == 0:
            strg.append([arr[i][j],10**(len(arr[i])-1-j)])
strg.sort(key= lambda x:x[1],reverse=True)
num = 9
ans = 0
for i in range(len(strg)):
    ans += strg[i][1]*num
    num-=1
print(ans)

