n = int(input())
seat = input()
ans = len(seat)+1
skip=50
for i in range(0,len(seat)-1):
    if i==skip:
        continue
    if seat[i:i+2]=='LL':
        ans -= 1
        skip = i+1
if ans > n:
    ans=n
print(ans)