a = list(range(1,9))
b = list(range(8,0,-1))

arr = list(map(int,input().split()))
if arr == a:
    print('ascending')
elif arr == b:
    print('descending')
else:
    print('mixed')

#2
# print({"12345678":"ascending","87654321":"descending"}.get(input()[::2],"mixed"))