a = 1000-int(input())
array = [500,100,50,10,5,1]
cnt = 0
for i in array:
    cnt += a//i
    a %= i
print(cnt)