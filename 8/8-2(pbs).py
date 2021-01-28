n=int(input())
room=1
plus=6
count=1

if n==1:
    print("1")
else:
    while True:
        room+=plus
        count+=1
        if n<=room:
            print(count)
            break
        plus+=6
