room = 2 
six = 6
six1 = 7
inp = int(input())

if inp == 1:
    print(1)

else:
    while(True):
        if inp <= six1:
            print(room)
            break
        else:
            room +=1
            six += 6
            six1 += six
