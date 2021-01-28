a, b, c = map(int, input().split())
if b>=c:
    print("-1")
else:
    print(int(a/(c-b)+1))

#a, b, c = map(int, input().split())
#res = 0
#while True:
#   if a+b*res>=c*res:
#       res+=1
#   else:
#       break
#print(res)         시간초과된 풀이
