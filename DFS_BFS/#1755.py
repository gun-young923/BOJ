#1755 숫자놀이 
"""
문제
79를 영어로 읽되 숫자 단위로 하나씩 읽는다면 "seven nine"이 된다. 
80은 마찬가지로 "eight zero"라고 읽는다. 
79는 80보다 작지만, 영어로 숫자 하나씩 읽는다면 "eight zero"가 "seven nine"보다 사전순으로 먼저 온다.

문제는 정수 M, N(1 ≤ M ≤ N ≤ 99)이 주어지면 
M 이상 N 이하의 정수를 숫자 하나씩 읽었을 때를 기준으로 사전순으로 정렬하여 출력하는 것이다.

입력
첫째 줄에 M과 N이 주어진다.

출력
M 이상 N 이하의 정수를 문제 조건에 맞게 정렬하여 한 줄에 10개씩 출력한다.

예제 입력 1 
8 28

예제 출력 1 
8 9 18 15 14 19 11 17 16 13
12 10 28 25 24 21 27 26 23 22
20
"""
# 1 72ms
""" import sys
input = sys.stdin.readline
dic = {'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five',
        '6':'six','7':'seven','8':'eight','9':'nine'}
m,n = map(int, input().split())
arr = list(map(str, range(m,n+1)))
temp = []
for i in arr:
    word=""
    for j in i:
        word += dic[j]
    temp.append([i,word])

temp.sort(key=lambda x: x[1])
cnt = 0
for i in temp:
    cnt += 1
    if cnt == 10:
        cnt = 0
        print(i[0],end='\n')    
    else:
        print(i[0],end=' ') """
        
# 2     68ms (dic 에 숫자별 영어 사전순 대로 정렬)
dic=[9,4,8,7,2,1,6,5,0,3]
m,n=map(int,input().split())        # 만약 한자리가 '8','eight' 이면 dic[8]값인 0으로 제일 우선순위
arr=sorted(list(map(str, range(m,n+1))),key=lambda x:[dic[int(j)]for j in x])
cnt = 0
for i in arr:
    cnt += 1
    if cnt == 10:
        cnt = 0
        print(i,end='\n')
    else:
        print(i,end=' ')