import sys

a = sys.stdin.readline().strip()
x = a.count('01')
y = a.count('10')
if x==y :
    cnt = x
elif x > y :
    cnt = x
else :
    cnt = y
print(cnt)
