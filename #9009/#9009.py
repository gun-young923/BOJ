t = int(input())
f=[0,1]
for i in range(2,46):
    f.append(f[i-1]+f[i-2])
f.reverse()
for i in range(t):
    n = int(input())
    l=[]
    for i in range(46):
        if n>=f[i]:
            l.append(f[i])
            n-=f[i]
            if n==0:
                break
    print(" ".join(map(str, l[::-1])))

#피보나치수열
""" f=[0,1]
def fib(n):
    for i in range(n):
        if n<len(f):
            return f[n]
        else:
            f.append(fib(n-1)+fib(n-2))
    return f[n]
print(fib(40)) """