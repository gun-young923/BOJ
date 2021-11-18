n, k = list(map(int, input().split()))
cnt=0
array=[]
for i in range(n):
    array.append(int(input()))
for i in array[::-1]:
    """ if i > k:
        continue """
    cnt += k//i
    k %= i
print(cnt)

