#10814 나이순정렬
"""
문제
온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다. 
이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 온라인 저지 회원의 수 N이 주어진다. (1 ≤ N ≤ 100,000)

둘째 줄부터 N개의 줄에는 각 회원의 나이와 이름이 공백으로 구분되어 주어진다. 
나이는 1보다 크거나 같으며, 200보다 작거나 같은 정수이고, 이름은 알파벳 대소문자로 이루어져 있고, 길이가 100보다 작거나 같은 문자열이다. 
입력은 가입한 순서로 주어진다.

출력
첫째 줄부터 총 N개의 줄에 걸쳐 온라인 저지 회원을 나이 순, 나이가 같으면 가입한 순으로 한 줄에 한 명씩 나이와 이름을 공백으로 구분해 출력한다.

예제 입력 1         예제 출력 1 
3                   20 Sunyoung
21 Junkyu           21 Junkyu
21 Dohyun           21 Dohyun
20 Sunyoung
"""

""" import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    a,b = input().rstrip().split()
    arr.append((int(a),b))
arr.sort(key=lambda x: x[0])
for i in arr:    
    print(i[0],i[1]) """

# 시간은 약간 더 빠르다
import sys
input = sys.stdin.readline

n = int(input())
temp = [[] for _ in range(201)]
for i in range(n):
    age,name = input().split()
    temp[int(age)].append(age+' '+name)
for i in temp:    
    if i == []:
        continue
    print('\n'.join(i))
