I=input
for t in range(int(I())):
    input()
    s=[v=='B' for v,w in zip(I(),I())if v!=w]
    v,w=sum(s),len(s)
    print(w-min(v,w-v))

    """ for i in range(int(input())):
    n = int(input())
    arr1 = list(input())
    arr2 = list(input())

    diff = [(a,b) for a,b in zip(arr1,arr2) if a!=b]
    print(max(diff.count(('W','B')),diff.count(('B','W')))) """