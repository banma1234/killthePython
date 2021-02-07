n, m = map(int, input().split())
board=[list(map(str, input())) for i in range(n)]

res=[]
for i in range(n-7):
    for j in range(m-7):
        Wcount=0
        Bcount=0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l)%2==0:
                    if board[k][l]!='W':
                        Wcount+=1
                    if board[k][l]!='B':
                        Bcount+=1
                else:
                    if board[k][l]!='B':
                        Wcount+=1
                    if board[k][l]!='W':
                        Bcount+=1
        res.append(Wcount)
        res.append(Bcount)
print(min(res))
