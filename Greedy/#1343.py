import sys
input = sys.stdin.readline

cnt,flag=0,0
arr = list(input().rstrip())
for i in range(len(arr)):
    
    if i==len(arr)-1 and arr[i]=='X':
        cnt+=1
        if cnt%2!=0:
            flag=1
            break
        a = cnt//4
        b = cnt%4//2
        arr[i-cnt+1:i+1] = 'AAAA'*a+'BB'*b
    elif arr[i]=='X':
        cnt+=1
    elif arr[i]!='X':
        if cnt%2!=0:
            flag=1
            break
        a = cnt//4
        b = cnt%4//2
        arr[i-cnt:i] = 'AAAA'*a+'BB'*b
        cnt=0
if flag==1:
    print(-1)
else:
    for i in range(len(arr)):
        print(arr[i],end='')