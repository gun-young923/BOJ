# 미완성 시간초과 / 메모리 초과

# bfs
""" import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())         # 직원수 (승범포함)
line = list(map(int, input().split()))  # 사수
# n -> 1 ~ n 까지
stat = dict()
for i in range(1,n+1):
    stat[i] = 0

link = [[] for _ in range(n+1)]
for i in range(1,n):                    # link[사수인덱스] 에 부사수번호 append
    link[line[i]].append(i+1)
# print(link)
def bfs(x,cnt):
    q = deque()
    q.append((x,cnt))
    while q:
        print(q)
        x,cnt = q.popleft()
        stat[x] += cnt
        for j in link[x]:   # 부사수들
            q.append((j,cnt))
    return

for i in range(m):
    temp = list(map(int, input().split()))
    if temp[0] == 1:
        bfs(temp[1],temp[2])
        # print(stat)
    if temp[0] == 2:
        print(stat[temp[1]]) """


# dfs
""" import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int, input().split())         # 직원수 (승범포함)
line = list(map(int, input().split()))  # 사수
# n -> 1 ~ n 까지
stat = dict()
for i in range(1,n+1):
    stat[i] = 0

link = [[] for _ in range(n+1)]
for i in range(1,n):                    # link[사수인덱스] 에 부사수번호 append
    link[line[i]].append(i+1)
# print(link)
def dfs(x,cnt):
    stat[x] += cnt
    for j in link[x]:   # 부사수들
        if j == 0:
            return
        dfs(j,cnt)
    return

for i in range(m):
    temp = list(map(int, input().split()))
    if temp[0] == 1:
        dfs(temp[1],temp[2])
        # print(stat)
    if temp[0] == 2:
        print(stat[temp[1]]) """


# ver.1  (76ms)

k = int(input())
F = input()
M = input()
total = len(M)
same = 0
for i in range(total):
  if F[i] == M[i]:
    same += 1

if same == 0:
  print(total-k)
elif same == total:
  print(k)
else:
  if same < k:
    print(total+same-k)
  else:
    print(total-same+k)