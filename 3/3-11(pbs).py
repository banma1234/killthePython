n, x = map(int, input().split())
arr=list(map(int, input().split()))

#배열 arr를 한줄에 출력하기 위해 list 안에 map을 취하고
#배열에 입력되는 값을 정수로 설정하기 위해 int를 취했다.

for i in range(0,n):
    if arr[i]<x:
        print(arr[i], end=" ")
        #출력 형식을 위해 end=" "를 입력했다(결과값 사이에 공백이 출력됨).
