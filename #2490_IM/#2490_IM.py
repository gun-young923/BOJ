for i in range(3):
    arr = list(map(int, input().split()))
    if arr.count(0)==0:
        print('E')
    else:
        print(chr(64+arr.count(0)))