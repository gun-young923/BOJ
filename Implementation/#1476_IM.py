e,s,m = map(int, input().split())
ans = 0
while(1):
    if (28*ans+s-e)%15==0 and (28*ans+s-m)%19==0:
        break
    else :
        ans += 1
print(ans*28+s)