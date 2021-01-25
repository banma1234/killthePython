case = int(input())
min=1000001
max=-1000001
arr=list(map(int, input().split()))
for i in arr:
    if i<min:
        min=i
    if i>max:
        max=i
print(min, max)

#   num = int(input())
#   arr = list(map(int, input()))
#   print(min(arr), max(arr))

# C에 뇌가 절여져서 코드가 길어졌다. 파이썬엔 기본 제공되는 기능 함수들이 많다.
