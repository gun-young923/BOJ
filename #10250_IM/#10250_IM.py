#2
for _ in range(int(input())):    
    f,r,n = map(int, input().split())    
    print("%d%02d" % ((n-1)%f+1, (n-1)//f+1))