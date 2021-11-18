import sys
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr = list(set(arr))
arr.sort()  #set()는 중복제거 but 순서상관없이 나와서 sort를 사용해 정렬해줘야 한다.
arr_sub = []
for i in range(len(arr)-1):
    arr_sub.append(arr[i+1]-arr[i]) 
arr_sub.sort()
if k >= len(arr):
    print(0)
else:
    for _ in range(k-1):
        arr_sub.pop()
    print(sum(arr_sub))
