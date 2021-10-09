n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s = 0
a.sort(reverse=True)
for i in range(n):
    num = b.index(min(b))
    s += a[i]*b[num]
    b.pop(b.index(min(b)))
print(s)