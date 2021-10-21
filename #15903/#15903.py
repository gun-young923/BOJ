# 최소 힙 사용
import heapq, sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int, input().split()))
heapq.heapify(arr)

for _ in range(m):
    ans = heapq.heappop(arr) + heapq.heappop(arr)
    heapq.heappush(arr,ans)
    heapq.heappush(arr,ans)
print(sum(arr))