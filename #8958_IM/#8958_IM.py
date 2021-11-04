#1
""" def cul(a):
    return sum(list(range(a+1)))

import sys
input = sys.stdin.readline
for _ in range(int(input())):
    
    arr = input().rstrip()
    ans , i= 0 , 0
    while(1):
        A = arr[i:] 
        if A.find('X') == -1:
            ans += cul(len(A))
            break
        ans += cul(A.find('X'))
        i += A.find('X')+1
    print(ans)
 """