a = int(input())
b = int(input())
c = int(input())

result = list(str(a * b * c))   # 숫자 배열을 문자열화 시킨 후 그대로 출력
for i in range(10):
    print(result.count(str(i)))
