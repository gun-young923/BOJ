def fac(a):
    if a == 0:
        return 1
    else:
        return a * fac(a-1)
    
print(fac(int(input())))