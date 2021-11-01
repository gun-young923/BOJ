word = input().upper()
arr=[]
for i in range(26):
    arr.append(word.count(chr(i+65)))
print('?'if arr.count(max(arr))>1 else chr(arr.index(max(arr))+65))    