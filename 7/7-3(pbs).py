s = list(map(str, input()))
arr=list('abcdefghijklmnopqrstuvwxyz')
for i in range(26):
    if arr[i] in s:
        print(s.index(arr[i]), end=" ")
    else:
        print("-1", end = " ")
