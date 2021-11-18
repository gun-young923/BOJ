#1
import sys
input = sys.stdin.readline

n,k = map(int, input().split())
arr = list(range(1,n+1))
ans = []
start = 0
print('<',end='')
for i in range(n):
    start = (start+k-1)%len(arr)
    ans.append(arr.pop(start))
    if i == n-1:
        print(ans[i],end='')
    else :
        print(ans[i],end=', ')
print('>')

#2    
""" import sys
input = sys.stdin.readline

n,k = map(int, input().split())
arr = list(range(1,n+1))
ans = []
start = 0
for i in range(n):
    start = (start + k-1)%len(arr)    
    ans.append(str(arr.pop(start)))
print('<'+', '.join(ans)+'>')
 """

