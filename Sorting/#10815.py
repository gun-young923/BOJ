#10815 숫자카드
"""
문제
숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 
정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 
둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다. 
두 숫자 카드에 같은 수가 적혀있는 경우는 없다.

셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 
넷째 줄에는 상근이가 가지고 있는 숫자 카드인지 아닌지를 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 
이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다

출력
첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 가지고 있으면 1을, 아니면 0을 공백으로 구분해 출력한다.

예제 입력 1                 예제 출력 1
5                           1 0 0 1 1 0 0 1
6 3 2 10 -10
8
10 9 -5 2 3 4 5 -10
"""

# 이진탐색 Binary_Search
import sys
input = sys.stdin.readline

n = int(input())
arr_n = list(map(int, input().split()))
m = int(input())
arr_m = list(map(int, input().split()))
temp = {i:0 for i in arr_m}

        # 재귀함수 이진탐색 3708ms                  # 1
''' def binary_search(arr,s,e,target):
    if s > e:
        return
    mid = (s+e)//2
    if arr[mid] == target:
        temp[arr[mid]] += 1
    elif arr[mid] < target:
        binary_search(arr,mid+1,e,target)
    else:
        binary_search(arr,s,mid-1,target)
    return '''

        # 반복문 이진탐색 2908ms                    # 2
def binary_search(arr,s,e,target):
    while s <= e:
        mid = (s+e)//2
        if arr[mid] == target:
            temp[arr[mid]] += 1
            return
        elif arr[mid] < target:
            # binary_search(arr,mid+1,e,target)
            s = mid + 1
        else:
            # binary_search(arr,s,mid-1,target)
            e = mid - 1
    return

cnt = 0
arr_n.sort()
for i in sorted(arr_m):
    binary_search(arr_n,0,n-1,i)
for i in temp.values():
    print(i,end=' ')

# 일반 정답 2   408ms
""" import sys
input = sys.stdin.readline

def sol():
    n = input()
    arr = set(input().split())  # list형식으로 입력받으면 시간초과 생김/ set()사용!
    m = input()
    ans = ""
    for i in input().split():
        if i in arr:
            ans += "1 "         # 바로 print(1,end=' ') 보다 빠르다...
        else:
            ans += "0 "
    print(ans)
sol() """

# 정답 3 (표현만다름)   412ms
""" import sys
input = sys.stdin.readline

input()
a=set(input().split())
input()
print(' '.join(['1' if j in a else '0' for j in input().split()])) """

#-----------------------------------------------------------------------------

# 아래 2개 시간초과 실패
""" import sys
input = sys.stdin.readline

n = int(input())
arr_n = list(map(int, input().split()))
m = int(input())
arr_m = list(map(int, input().split()))
# temp = {i:0 for i in arr_m}
# for i in temp:
#     temp[i] = 1 if i in arr_n else 0
# for i in temp.values():
#     print(i,end=' ')

for i in arr_m:
    if i in arr_n:
        print(1,end=' ')
    else:
        print(0,end=' ') """


""" import sys
input = sys.stdin.readline

n = int(input())
arr_n = sorted(list(map(int, input().split())))
m = int(input())
arr_m = sorted(list(map(int, input().split())))
temp = {i:0 for i in arr_m}
# print('\n\n')
# print(arr_n)
# print(arr_m)
# print('\n\n')
cnt = 0
for i in range(m):
    for j in range(len(arr_n[cnt:])):
        # print('----',i,j,cnt,'----')
        # print('----',arr_m[i],arr_n[cnt:][j],'----')
        if arr_m[i] > arr_n[cnt:][j]:
            continue
        elif arr_m[i] == arr_n[cnt:][j]:
            temp[arr_m[i]] += 1
            cnt += j+1
            break
        else:
            cnt += j
            break
for i in temp.values():
    print(i,end=' ') """

