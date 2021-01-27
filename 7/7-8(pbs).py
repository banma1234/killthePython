arr = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = list(map(str, input()))
sum=0
for i in range(len(word)):
  for j in range(8):
    if word[i] in arr[j]:
        sum+=j+3
print(sum)
