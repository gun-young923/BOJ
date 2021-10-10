t = int(input())
cnt = []
array = [300, 60,10]
for i in array:
    cnt.append(t//i)
    t %= i
if t != 0:
    print(-1)
else :
    print(cnt[0],cnt[1],cnt[2])