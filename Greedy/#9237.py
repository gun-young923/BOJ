n = int(input())
arr = sorted(list(map(int, input().split())),reverse=1)
for i in range(n):
    arr[i]= arr[i]-n+i
print(max(arr)+2+n)

#1
""" n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
total = 1+arr[0]+1
for i in range(1,n):
    total = max(total,arr[i]+i+2)
print(total) """

