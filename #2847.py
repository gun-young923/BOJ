import sys

cnt = 0
n = int(sys.stdin.readline())
array = [int(sys.stdin.readline()) for _ in range(n)]
# i는 n-1부터 1까지 (큰수부터 내림차순으로 -1은 꼭 써줘야함)
for i in range(n-1,0,-1): 
    if array[i] <= array[i-1]:
        cnt += array[i-1] - (array[i]-1)
        array[i-1] = array[i]-1
print(cnt)
