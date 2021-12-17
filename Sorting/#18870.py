#18870 좌표압축
"""
문제
수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.

Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.

X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.

입력
첫째 줄에 N이 주어진다.

둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.

출력
첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다.

제한
1 ≤ N ≤ 1,000,000
-109 ≤ Xi ≤ 109

예제 입력 1                     예제 출력 1 
5                               2 3 0 3 1
2 4 -10 4 -9


예제 입력 2                     예제 출력 2 
6
1000 999 1000 999 1000 999      1 0 1 0 1 0
"""

# 1 시간초과
""" import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))


for i in arr:
    cnt = 0
    temp = {i:0 for i in set(arr)}
    for j in arr:
        if i == j:
            continue
        if i > j:
            if temp[j] != 1:
                temp[j] = 1
                cnt += 1
    print(cnt,end=' ') """

# 2 시간초과
""" import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
temp = sorted(list(set(arr)))
for i in arr:
    cnt = len(temp[:temp.index(i)])
    print(cnt,end=' ') """

# 3 통과 2276ms
# list.index() -> 시간복잡도 O(N)
# dict() 형태로 저장하면 O(1)로 시간 줄인다.

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

temp = sorted(list(set(arr)))
dic = {temp[i]:i for i in range(len(temp))}
for i in arr:
    print(dic[i], end=' ')