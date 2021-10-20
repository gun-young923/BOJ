import sys
input = sys.stdin.readline

n = int(input())
arr = input().rstrip()
#pPAp 만 인정
st,ind = 0,0
cnt = 0
while 1:
    ind = arr.find('pPAp',st)
    if ind==-1:break
    cnt += 1
    st = ind+4
print(cnt)