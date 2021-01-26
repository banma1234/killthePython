def hansu(n):
    count=0
    if n<100:
        return n
    elif 100<=n<=1000:
        for i in range(100, n+1):
            arr=list(map(int, str(i)))
            if arr[0] - arr[1] == arr[1] - arr[2]:
                count+=1
        return 99+count

num=int(input())
print(hansu(num))
