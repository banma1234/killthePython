def star(n, x, y):
    if n==1:
        arr[y][x]='*'
    else:
        next=n//3
        for i in range(3):
            for j in range(3):
                if i!=1 or j!=1:
                    star(next, x+j*next, y+i*next)

num=int(input())
arr=[[' ' for i in range(num)] for j in range(num)]
star(num, 0, 0)
for i in arr:
    print(''.join(i))
