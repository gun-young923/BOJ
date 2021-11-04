import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()
print(int(round(sum(arr)/n,0))) # 소수점 첫째자리에서 반올림
print(arr[n//2])
cnt = Counter(arr) 
cnt = sorted(cnt.items(), key=lambda x: (-x[1]))
if n==1:                    #n==이면 cnt 는 값이 1개라 아래 조건문 실행시 오류발생
    print(arr[0])
elif cnt[0][1]==cnt[1][1]:
    print(cnt[1][0])
else:
    print(cnt[0][0])
print(arr[-1]-arr[0])
