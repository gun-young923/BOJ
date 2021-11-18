import sys

case = int(sys.stdin.readline())
for test_case in range(case):
    num = int(sys.stdin.readline())
    array =[0]* (num)
    for _ in range(num):
        i,j = map(int,sys.stdin.readline().split()) 
        array[i-1]=j
    cnt = 1
    a = array[0]
    for i in array[1:]:
        if i < a:
            cnt+=1
            a = i
    print(cnt)
