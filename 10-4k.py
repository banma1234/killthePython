def hanoi(t, a, b, c):
    if t == 1:
        print(a, c)
    else:
        hanoi(t - 1, a, c, b)
        print(a, c)
        hanoi(t - 1, b, a, c)

t = int(input())        
count = 2**t -1
print(count)
hanoi(t, 1, 2, 3)
