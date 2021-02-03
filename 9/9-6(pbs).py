def eratostenes(n):
    arr=[True]*n
    m=int(n**0.5)
    for i in range(2, m+1):
        if arr[i]==True:
            for j in range(i*2, n, i):
                arr[j]=False
    return [i for i in range(2, n) if arr[i]==True]

def goldbah(n):
    arr=eratostenes(n)
    m=max([i for i in range(len(arr)) if arr[i]<=n/2])
    for i in range(m, -1, -1):
        for j in range(i, len(arr)):
            if arr[i]+arr[j]==n:
                return [arr[i], arr[j]]

for i in range(int(input())):
    num=int(input())
    arr=goldbah(num)
    print(arr[0], arr[1])
