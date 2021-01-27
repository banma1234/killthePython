case=int(input())
for i in range(case):
    arr=input().split()
    num=int(arr[0])
    res=list(map(str, arr[1]))
    for j in range(len(res)):
        print(res[j]*num, end="")
    print()
