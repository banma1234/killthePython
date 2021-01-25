testCase = int(input())

for i in range(testCase):
    problemResult = input()
    score = 0
    sumScore = 0
    for k in problemResult:
        if k == "O":
            score += 1
        else:
            score = 0
        sumScore += score
    print(sumScore)
