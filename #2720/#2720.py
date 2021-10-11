import sys
total=[]
s = []
case = int(sys.stdin.readline())
for i in range(case):
    s.append([])
    total = int(sys.stdin.readline())
    s[i].append(total//25)
    s[i].append(total%25//10)
    s[i].append(total%25%10//5)
    s[i].append(total%25%10%5) 
for i in range(case):
    print(s[i][0],s[i][1],s[i][2],s[i][3])
