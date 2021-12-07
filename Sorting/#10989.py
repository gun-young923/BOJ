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
import sys
input = sys.stdin.readline

arr = [int(input()) for _ in range(int(input()))]
for i in range(len(arr)):
    min_index = arr[i:].index(min(arr[i:]))
    arr[i] , arr[min_index+i] = arr[min_index+i], arr[i]
print(arr)