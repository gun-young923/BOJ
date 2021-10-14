for _ in range(int(input())):
    arr=[]
    a,b = input().split()
    for x,y in zip(a,b):
        if x!=y:
            arr.append([x,y])
    print(max(arr.count(['1','0']),arr.count(['0','1'])))