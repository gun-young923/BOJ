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

 #2
""" import sys
input = sys.stdin.readline
for _ in range(int(input())):
    arr = input()
    cnt = 1
    ans = 0
    for i in arr:
        if i is 'O':
            ans += cnt
            cnt += 1
        else:
            cnt = 1
    print(ans) """

#3
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    arr = input().rstrip().split('X') #'X'별로 나눠서 'O'만 모아서 계산
    ans = 0
    for i in arr:
        ans += sum(list(range(len(i)+1)))
    print(ans)
