def eratostenes(n):
    arr=[True]*n
    m=int(n**0.5)
    for i in range(2, m+1):
        if arr[i]==True:
            for j in range(i*2, n, i):
                arr[j]=False
    return [i for i in range(2, n) if arr[i]==True]
    # 2부터 n까지의 수를 i에 대입하여 반환하되 arr[i]가 True인 경우에만 반환한다.

while True:
    case=int(input())
    if case==0: break
    arr=eratostenes(2*case+1)
    print(len([i for i in arr if i>case]))


# 시간 초과된 예제(time over)

#while True:
#    case=int(input())
#    if case==0: break
#    else:
#        arr=[]
#        for i in range(case+1, case*2+1):
#            if i==1:
#                continue
#            elif i==2:
#                arr.append(i)
#            else:
#                for j in range(2, i):
#                    if j>=i-1:
#                        arr.append(i)
#                    if i%j==0:
#                        break
#        print(len(arr))
