#1
""" a,b = map(list,input().split())
a.reverse()
b.reverse()
for i in max(a,b):
    print(i,end='') """

#2
a,b = input().split()
print(max(a[::-1],b[::-1]))