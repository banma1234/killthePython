case=int(input())
numlist=[int(input()) for i in range(case)]
numlist.sort()
for i in range(case):
    print(numlist[i])
