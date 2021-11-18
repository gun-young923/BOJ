#1
""" for _ in range(int(input())):    
    f,r,n = map(int, input().split())
    if n%f == 0:
        a = str(f)
        if n//f < 10:
            b = '0'+str(n//f)
        else:
            b = str(n//f)
    else:
        a = str(n%f)
        if n//f+1 < 10:
            b = '0'+str(n//f+1)
        else:
            b = str(n//f+1)
    print(a+b) """

#2
for _ in range(int(input())):    
    f,r,n = map(int, input().split())    
    print("%d%02d" % ((n-1)%f+1, (n-1)//f+1))

