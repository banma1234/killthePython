n = int(input())
a = []
for i in range(0, n):
    a.append(int(input()))
b = sorted(a)
for k in range(0, n):
    print(b[k])
