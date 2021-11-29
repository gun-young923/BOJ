a,b,n,m = map(int, input().split())

cnt = 0
max_val = max(a,b)
min_val = min(a,b)
if n > m:
    cnt += (n-m)//max_val
    r = (n-m)%max_val
    cnt += r//min_val
    cnt += r%min_val
    print(cnt)

else:
    

    pass
""" 
a배 위치
b배 위치 
+a 의 위치
+b 의 위치 
+-1
"""