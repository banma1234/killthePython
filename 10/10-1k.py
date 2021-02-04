#import math
#print(math.factorial(int(input())))

def f(n):
    if n <= 1:
        return 1
    else:
        return n* f(n-1)
print(f(int(input())))
