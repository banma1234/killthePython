
def d (n):
    r = n
    for i in list(str(n)):
        r += int(i)
    return int(r)
    
arr = []

for x in range(1, 10001):
    arr.append(d(x))
    if x not in arr:
        print(x)

