case = int(input())
score = list(map(int, input().split()))
M = max(score)
nscore = []
for i in score:
    nscore.append(i/M*100)
print(sum(nscore)/len(nscore))
