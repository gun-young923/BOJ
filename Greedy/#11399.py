n = int(input())
t = list(map(int, input().split()))
t.sort()        #t.sort() = 영구적 원본변화 // sorted(t) = 일시적 원본변화X
s = 0

for i in range(1,n+1):
    s += sum(t[0:i])
print(s)