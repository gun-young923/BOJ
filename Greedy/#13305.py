import sys
n = int(sys.stdin.readline())
dist = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))

result = 0
a = cost[0]
for i in range(len(dist)):
    if a > cost[i]:
        a = cost[i]
    result += a*dist[i]    
print(result)