H, M = map(int, input().split())
if M-45>=0:
    M-=45
    print(H, M)
elif M-45<0:
    M=60-(45-M)
    if H-1<0:
        H=23
    else:
        H-=1
    print(H, M)
