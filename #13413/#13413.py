I=input
for t in range(int(I())):
    input()
    s=[v=='B' for v,w in zip(I(),I())if v!=w]
    v,w=sum(s),len(s)
    print(w-min(v,w-v))