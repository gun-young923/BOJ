#10816 숫자카드2
"""
문제
숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 
정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 
둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 
넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 
이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

출력
첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지를 공백으로 구분해 출력한다.

예제 입력 1                      예제 출력 1 
10                              3 0 0 1 2 0 0 2
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10
"""

#1 일반 정답 1112ms
""" import sys
input = sys.stdin.readline

n = int(input())
arr_n = list(map(int, input().split()))
m = int(input())
arr_m = list(map(int, input().split()))
# print('------------------------------------')
temp = dict()
for i in arr_n:
    if i not in temp.keys():
        temp[i] = 0
    temp[i] += 1
# print(temp)
arr_n = set(arr_n)
# print(arr_n)
ans = ""
for i in arr_m:
    if i in arr_n:
        ans += str(temp[i]) + ' '
    else:
        ans += '0 '
print(ans)
 """

#2 이진탐색 Binary_Search        3280ms
""" import sys
input = sys.stdin.readline

n = int(input())
arr_n = list(map(int, input().split()))
m = int(input())
arr_m = list(map(int, input().split()))
#1
temp = dict()
for i in arr_n:
    if i not in temp.keys():
        temp[i] = 0
    temp[i] += 1
arr_n = list(set(arr_n))
#2  count 떄문인지 몰라도 시간초과
'''
temp = {i:arr_n.count(i) for i in arr_n}
# print(temp)
'''
# 반복문 이진탐색 
def binary_search(arr,s,e,target):
    while s <= e:
        mid = (s+e)//2
        if arr[mid] == target:
            # temp[arr[mid]] += 1
            return str(temp[arr[mid]])+' '
        elif arr[mid] < target:
            s = mid + 1
        else:
            e = mid - 1
    return '0 '

cnt = 0
arr_n.sort()
ans = ""
for i in arr_m:
    ans += binary_search(arr_n,0,len(arr_n)-1,i)
print(ans) """

#3 Counter 사용 928ms / Counter사용 시 output = dict()형식 {a:b,...}
import sys
from collections import Counter
input = sys.stdin.readline

input()
cnt = Counter(input().split())
input()
arr_m = input().split()
# print('------------------------------------')
ans=""
for i in arr_m:
    if i in cnt.keys():
        ans += str(cnt[i]) + ' '
    else:
        ans += '0 '
print(ans)

# 가장 빠른 답  564ms
""" import sys
from collections import Counter
input = sys.stdin.readline

input()
cnt = Counter(input().split())
input()
print(' '.join(str(cnt[m]) if m in cnt else '0' for m in input().split())) """
