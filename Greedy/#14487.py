n = int(input())
cost = list(map(int,input().split()))
cost.pop(cost.index(max(cost)))
print(sum(cost))