#1427 소트인사이드
"""
문제
배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

입력
첫째 줄에 정렬하려고 하는 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.

예제 입력 1     예제 출력 1 
2143            4321

예제 입력 2     예제 출력 2 
999998999       999999998

예제 입력 3     예제 출력 3 
61423           64321

예제 입력 4     예제 출력 4
500613009       965310000
"""
# 내림차순 정렬
print(''.join(sorted(list(input().rstrip()),reverse=True)))