import sys
array = [-1]*3
i=0
cnt = []
while(1):
    
    array = list(map(int, sys.stdin.readline().split()))
    if array[2] == 0:
        break
    a = array[2]//array[1]
    r = array[2]%array[1]
    cnt.append(a*array[0])
    if r < array[0]:
        cnt[i] += r
    else:
        cnt[i] += array[0]
    i+=1


for i in range(1,len(cnt)+1):
    print('Case %d: %d' %(i,cnt[i-1]))