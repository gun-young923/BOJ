import sys
from collections import deque
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n,m = map(int,input())
arr = [list(map(int, input().split())) for _ in range(n)]
