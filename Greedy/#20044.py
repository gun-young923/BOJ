n = int(input())
s = list(map(int, input().split()))
s.sort()
sol = s[0] + s[2*n-1]
for i in range(1,n):
    if sol > s[i] + s[2*n-i-1]:
        sol = s[i] + s[2*n-i-1]
print(sol)
