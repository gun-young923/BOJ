# a = 97 / z = 122
w = list(map(ord, input()))
ans = ['0']*26
for i in w:
    if ans[i-97] != '0':
        continue
    ans[i-97] = str(w.count(i))
print(' '.join(ans))