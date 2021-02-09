import sys
case=int(sys.stdin.readline())  # sys 모듈의 입출력 함수를 사용하면 입출력에 소모되는 메모리가 크게 절약된다.

count=[0]*10001
for i in range(case):
    count[int(sys.stdin.readline())]+=1
for i in range(10001):
    if count[i]!=0:
        for j in range(count[i]):
            print(i)

# 메모리 초과된 예제
# 배열의 크기나 반복회수를 줄이는것 보다 입출력시의 메모리 할당을 줄이는게 더 경제적이다.

#case=int(input())
#numlist=[int(input()) for i in range(case)]

#count=[0 for i in range(max(numlist)+1)]
#for i in range(case):
#    count[numlist[i]]+=1
#for i in range(max(numlist)+1):
#    for j in range(count[i]):
#        print(i)
