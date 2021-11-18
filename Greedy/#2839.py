n = int(input())
cnt1 = n//5
cnt2 = 0
n = n%5
while(cnt1>-1):  
    if n%3 == 0:
        cnt2 = n//3
        break
    cnt1 -= 1
    n += 5
if cnt1 < 0:
    print(-1)
else:        
    print(cnt1 + cnt2)