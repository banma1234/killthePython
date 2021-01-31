case=int(input())
floor=room=0
for i in range(case):
    h, w, n = map(int, input().split())
    if n%h==0:
        floor=h
        room=n//h
    else:
        floor=n%h
        room=n//h+1
    if room<10:
        print(floor, "0", room, sep="")
    else:
        print(floor, room, sep="")
