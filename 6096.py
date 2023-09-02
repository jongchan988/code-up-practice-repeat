panSize = 19
pan = [[0] * panSize for _ in range(panSize)]

for i in range(panSize):
    inputArr = input().split()
    for j in range(panSize):
        pan[i][j] = int(inputArr[j])

n = int(input())

for i in range(n):
    x, y = input().split()
    x = int(x) - 1
    y = int(y) - 1

    for j in range(panSize):
        pan[x][j] = 0 if pan[x][j] == 1 else 1
        pan[j][y] = 0 if pan[j][y] == 1 else 1

# 바둑판 상태 출력
for i in range(panSize):
    for j in range(panSize):
        print(pan[i][j], end=" ")
    print()