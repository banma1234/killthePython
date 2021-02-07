st = int(input())
li = []

for _ in range(st):
    w, h = map(int, input().split())
    li.append((w, h))

for i in li:
    c = 1
    for k in li:
        if i[0] != k[0] and i[1] != k[1]:
            if i[0] < k[0] and i[1] < k[1]:
                c += 1
    print(c, end=" ")
