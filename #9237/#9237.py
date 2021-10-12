n = int(input())
arr = sorted(list(map(int, input().split())),reverse=1)
for i in range(n):
    arr[i]= arr[i]-n+i
print(max(arr)+2+n)