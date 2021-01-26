def hansu(n):
    count=0
    if n<100:
        return n
    elif 100<=n<=1000:
        for i in range(100, n+1):
            hun=i//100
            ten=i//10%10
            one=i%10
            if hun-ten == ten-one:
                count+=1
        return 99+count

num=int(input())
print(hansu(num))
