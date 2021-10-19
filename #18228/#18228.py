import sys
input = sys.stdin.readline

n = int(input())           # 3 <= n <= 200000
arr_l,arr_r = input().split('-1')   
# 1 <= arr <= 1000000000 // loc of penguin == -1 (!= arr[0] or arr[n-1])
# -1 기준 양옆 나눠 최소값 더하면 답
arr_l = list(map(int, arr_l.split()))
arr_r = list(map(int, arr_r.split()))
print(min(arr_l)+min(arr_r))

