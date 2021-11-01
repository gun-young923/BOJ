a = list(range(1,9))
b = list(range(8,0,-1))

arr = list(map(int,input().split()))
if arr == a:
    print('ascending')
elif arr == b:
    print('descending')
else:
    print('mixed')