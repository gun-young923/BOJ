#11650 좌표정렬하기
"""
문제
2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, 
x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 
둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. 
(-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.

출력
첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.

예제 입력 1     예제 출력 1 
5               1 -1
3 4             1 1
1 1             2 2
1 -1            3 3
2 2             3 4
3 3
"""
# 1
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    x,y = map(int, input().rstrip().split())
    arr.append((x,y))
arr.sort(key=lambda x:(x,[0],x[1]))
for i in arr:
    print(i[0],i[1])

# 문자열로 숫자 비교 -> 절대안됨 (사전순 비교라 '10'은 '2'보다 작다라고 나온다.)
# '10' < '2'    True라고 한다. '2'가 '1'보다 큰 숫자이기 때문/ '10'은 '1'+'0' 으로 본다.
# ' '.join()을 쓸거면 아래처럼 int형 비교 후 str으로 변환 후 사용
""" import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    x,y = map(int, input().split())
    arr.append((x,y))
arr.sort(key=lambda x:(x[0],x[1]))
for i in arr:
    i = list(map(str, i))
    print(' '.join(i)) """