import sys
input = sys.stdin.readline

N = int(input())
a,b = map(int, input().split())
arr = list(map(int, input().split()))
pen = a*b
num,cnt = 0,0
arr.sort(reverse=True)
for i in arr:
    cnt += i
    num += 1
    if cnt >= pen:
        break
if cnt < pen:
    print("STRESS")
else:
    print(num)