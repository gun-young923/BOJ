# 10989 수 정렬하기3
"""
문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

예제 입력 1     예제 출력 1
10              1
5               1
2               2
3               2
1               3
4               3
2               4
3               5
5               5
1               7
7
"""

# 퀵정렬
""" import sys
input = sys.stdin.readline

def q_sort(arr):
    if len(arr) <= 1:
        return arr
    left = [x for x in arr[1:] if x <= arr[0]]
    right = [x for x in arr[1:] if x > arr[0]]
    arr = q_sort(left) + [arr[0]] + q_sort(right)
    return arr

arr = [int(input()) for _ in range(int(input()))]
for i in q_sort(arr):
    print(i) """

# 선택정렬
""" import sys
input = sys.stdin.readline

arr = [int(input()) for _ in range(int(input()))]
for i in range(len(arr)):
    min_index = arr[i:].index(min(arr[i:]))
    arr[i] , arr[min_index+i] = arr[min_index+i], arr[i]
print(arr) """

# 삽입정렬
""" import sys
input = sys.stdin.readline

arr = [int(input()) for _ in range(int(input()))]
for i in range(1,len(arr)):
    for j in range(i,0,-1):
        if arr[j] < arr[j-1]:
            arr[j-1] ,arr[j] = arr[j], arr[j-1]
        else:
            break
for i in arr:
    print(i) """

# 입력값을 리스트로 하지 않고 입력받을 수 있는 최대 수 +1 까지 리스트로 만들어
# 입력값에 해당하는 인덱스에 카운팅 후 맨앞부터 카운팅만큼 출력
import sys
input = sys.stdin.readline
n = int(input())
b = [0] * 10001
for i in range(n):
    b[int(input())] += 1
for i in range(10001):
    if b[i] != 0:
        for j in range(b[i]):
            print(i)