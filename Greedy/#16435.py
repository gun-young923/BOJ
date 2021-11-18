n,l = map(int,input().split())

for i in sorted(map(int, input().split())):
    if l>=i:
        l += 1
    else :
        break
print(l)

