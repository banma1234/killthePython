def disassamble(n):
    num=n
    res=0
    while num>=1:
        res+=num%10
        num//=10
    res+=n
    return res

num=int(input())
for i in range(num+1):
    if disassamble(i)==num:
        print(i)
        break
    elif i==num:
        print("0")
