def selfnum(n):  
    result = n
    while n != 0:
        result += n%10
        n //= 10
    return result
 
arr = []
 
for i in list(range(1,10001)):
  arr.append(selfnum(i))
  if i not in arr:
    print(i)
