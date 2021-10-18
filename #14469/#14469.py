n = int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int, input().split())))
arr.sort()
t = sum(arr[0])

for i in range(1,n):
    if arr[i][0] < t:
        t += arr[i][1]
    else :
        t = sum(arr[i])
print(t)