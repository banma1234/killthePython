import math
def p(n):
    if n ==1 :
        return False
    
    a = int(math.sqrt(n))
    for i in range(2, a+1):
        if n % i == 0 :
            return False
    return True

m, n = map(int, input().split())
for k in range(m, n+1):
    if p(k):
        print(k)
