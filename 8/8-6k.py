t = int(input())

for i in range(t):  
    floor = int(input())  
    num = int(input())  
    floor0 = [x for x in range(1 ,num+1)]
    for y in range(floor):
        for k in range(1, num):
            floor0[k] += floor0[k-1]
    print(floor0[-1])

    
