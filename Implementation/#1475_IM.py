a = input()
b = list(set(a))
arr = [0]*10
for i in b:
    arr[int(i)] = a.count(i)
dex = arr.index(max(arr))
ans = arr.pop(dex)
if dex == 6:
    n = (ans+arr[8]+1)//2
    if n >= max(arr):
        print(n)
    else:
        print(max(arr))
elif dex == 9:
    n = (ans+arr[6]+1)//2
    if n >= max(arr):
        print(n)
    else:
        print(max(arr))
else:
    print(ans)

#
""" s=input()
N=[s.count(str(i)) for i in range(10)]
N[6]=(N[6]+N[9]+1)//2;N[9]=N[6]
print(max(N)) """

##
""" n = input()
lst = []
for num in '0123456789':
    lst.append(n.count(num))
lst[6] = (lst[6]+lst[9]+1)//2
del lst[9]
print(max(lst)) """

###
""" d_n = list(map(int, input()))
d_list = []
for i in range(10):
    d_list.append(d_n.count(i))
d_list[6] = (d_list[6] + d_list[9] + 1)//2
del d_list[9]
print(max(d_list)) """