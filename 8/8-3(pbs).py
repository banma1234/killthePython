num=int(input())
count=0
x=0
while count<num:
    x+=1
    count+=x
count-=x
if x%2==0:
    i=num-count
    j=x-i+1
else:
    i=x-(num-count)+1
    j=num-count
print(i,"/",j, sep='')
