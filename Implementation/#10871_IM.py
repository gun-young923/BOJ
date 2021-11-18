#1
n, x = map(int, input().split())
arr = list(map(int, input().split()))
for i in arr:
    if i < x:
        print(i,end=" ")

""" #2
n,x = map(int,input().split())
ans = [i for i in input().split() if int(i)<x]
print(' '.join(ans)) """