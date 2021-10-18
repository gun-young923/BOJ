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