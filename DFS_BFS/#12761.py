from collections import deque
import sys
input = sys.stdin.readline

def sol():
    a,b,s,e = map(int,input().split())
    #bfs
    queue = deque()
    queue.append([s,0])
    book = dict()
    while queue:
        s,cnt = queue.popleft()
        temp = [s+1, s-1, s+a, s+b, s-a, s-b, a*s, b*s]
        for i in temp:
            if 0 <= i <= 100000 and i not in book.keys():
                answer = cnt +1
                if i == e:
                    return answer
                else:
                    book[i] = 1
                    queue.append([i,answer])
    
if __name__ =="__main__":
    print(sol())