# 타임테이블 리스트에 각 시간에 대응하는 인덱스에 사용하는 bucket수를 모두 합친다.
# 앞서 사용하고 사용가능한 bucket 임의의 a개는 다음에 사용할 것이며 
# 다음턴때 사용할 때 필요한 bucket수가 a보다 적건 많건 상관없다.
# a보다 적으면 a에서 꺼내 쓰면 되고 많으면 현재 필요한 수만큼 더 더해질 것이다 
import sys
input = sys.stdin.readline
arr=[]
ans=[0]*1000
n = int(input())
for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(arr[i][0],arr[i][1]):
        ans[j]+= arr[i][2]
print(max(ans))
    