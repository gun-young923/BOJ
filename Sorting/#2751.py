#2751 수 정렬하기2
"""
문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 
이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

예제 입력 1     예제 출력 1 
5               1
5               2
4               3
3               4
2               5
1
"""

# pypy3 776ms / python3 1356ms
import sys
input = sys.stdin.readline

""" for i in sorted([int(input()) for _ in range(int(input()))]):
    print(i) """
    
print('\n'.join(sorted([input().rstrip() for _ in range(int(input()))])))