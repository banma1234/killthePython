n = int(input())
count=0
while True:
    if n%5==0:
        count+=n//5
        break
    elif n%5!=0:
        n-=3
        count+=1
    if n==0:
        break
    if n<0:
        count=-1
        break
print(count)
