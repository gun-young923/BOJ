#11931 수정렬하기4
"""
문제
N개의 수가 주어졌을 때, 이를 내림차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

출력
첫째 줄부터 N개의 줄에 내림차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

예제 입력 1     예제 출력 1 
5               5
1               4
2               3
3               2
4               1
5
"""
import sys
input = sys.stdin.readline  
arr = sorted([int(input()) for _ in range(int(input()))],reverse=True)
print('\n'.join(map(str, arr)))
