#10825 국영수
"""
문제
도현이네 반 학생 N명의 이름과 국어, 영어, 수학 점수가 주어진다. 
이때, 다음과 같은 조건으로 학생의 성적을 정렬하는 프로그램을 작성하시오.

국어 점수가 감소하는 순서로
국어 점수가 같으면 영어 점수가 증가하는 순서로
국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 (단, 아스키 코드에서 대문자는 소문자보다 작으므로 사전순으로 앞에 온다.)
입력
첫째 줄에 도현이네 반의 학생의 수 N (1 ≤ N ≤ 100,000)이 주어진다. 
둘째 줄부터 한 줄에 하나씩 각 학생의 이름, 국어, 영어, 수학 점수가 공백으로 구분해 주어진다. 
점수는 1보다 크거나 같고, 100보다 작거나 같은 자연수이다. 이름은 알파벳 대소문자로 이루어진 문자열이고, 길이는 10자리를 넘지 않는다.

출력
문제에 나와있는 정렬 기준으로 정렬한 후 첫째 줄부터 N개의 줄에 걸쳐 각 학생의 이름을 출력한다.

예제 입력 1                     예제 출력 1 
12                              Donghyuk
Junkyu 50 60 100                Sangkeun    
Sangkeun 80 60 50               Sunyoung
Sunyoung 80 70 100              nsj
Soong 50 60 90                  Wonseob
Haebin 50 60 100                Sanghyun
Kangsoo 60 80 100               Sei
Donghyuk 80 60 100              Kangsoo
Sei 70 70 70                    Haebin
Wonseob 70 70 90                Junkyu
Sanghyun 70 70 80               Soong
nsj 80 80 80                    Taewhan
Taewhan 50 60 90
"""

""" import sys
input = sys.stdin.readline

arr = []
for i in range(int(input())):
    q,w,e,r = input().split()
    arr.append([q,int(w),int(e),int(r)])
arr.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))
for i in arr:
    print(i[0]) """

#-----------------------
import sys
input=sys.stdin.readline
n=int(input())
def sol(x):
    return (-int(x[1]),int(x[2]),-int(x[3]),x[0])
data=[sol(input().split()) for _ in range(n)]      
print(*map(lambda x:x[3],sorted(data)),sep='\n')    # sorted(data)의 4번째 원소들만 모아 출력