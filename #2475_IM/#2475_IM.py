arr = list(map(int, input().split()))
ans,cnt = 0,0
for i in arr:
    cnt += i**2
print(cnt%10)