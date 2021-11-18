a = list(map(int, input().split(' ')))
c = list(map(int, input().split(' ')))

b = []
x = c[0] - a[2]
y = int(c[1] / a[1])
z = c[2] - a[0]
b.append(x)
b.append(y)
b.append(z)

print(b[0],b[1],b[2])

'''
############### 다른 방법 ####################
I=lambda:map(int,input().split())
a,b,c=I()
d,e,f=I()
print(d-c,e//b,f-a)
'''