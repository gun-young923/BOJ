import sys
ucpc = input() 
try:
    ucpc = ucpc[ucpc.index('U'):]
    ucpc = ucpc[ucpc.index('C'):]
    ucpc = ucpc[ucpc.index('P'):]
    ucpc = ucpc[ucpc.index('C'):]
except:
    print("I hate UCPC") 
    sys.exit()
print("I love UCPC")


#1
""" arr = input()
n=[]
flag=0
for i in "UCPC":
    if arr.find(i)==-1:
        flag=-1
        break
    else :
        n.append(arr.find(i))
        arr = list(arr)
        arr = arr[arr.index(i)+1:]
        arr = str(arr)
    
if flag==-1:
    print("I hate UCPC")
else :
    print("I love UCPC") """