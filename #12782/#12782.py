for _ in range(int(input())):
    arr=[]
    a,b = input().split()
    for x,y in zip(a,b):
        if x!=y:
            arr.append([x,y])
    print(max(arr.count(['1','0']),arr.count(['0','1'])))

#1
""" for _ in range(int(input())):
    cnt1=0
    a,b = map(str,input().split())
    cnt = abs(a.count('1')-b.count('1'))
    for i in range(len(a)):
        if a[i]!=b[i]:
            cnt1+=1
    print(cnt + (cnt1-cnt)//2) """