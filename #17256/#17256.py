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