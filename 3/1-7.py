test = int(input())
for i in range(1, test+1):
    a, b = map(int, input().split())
    print("Case #%s: %s"%(i, a+b))
