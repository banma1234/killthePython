import math
case = int(input())
for i in range(case):
    x, y = map(int, input().split())
    distance = y - x
    if distance<=3:
        print(distance)
    else:
        num = int(math.sqrt(distance))
        if distance == num ** 2:
            print(2 * num - 1)
        elif num ** 2 < distance <= num ** 2 + num:
            print(2 * num)
        else:
            print(2 * num + 1)
