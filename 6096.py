panSize = 19


pan = []

for i in range(panSize):
    inputArr = input().split()
    pan.append(inputArr)

# 십자뒤집기 횟수
n = int(input())

for i in range(n):
    x, y = input().split()
    x = int(x) -1
    y = int(y) -1

    # 가로 뒤집기
    for j in range(panSize):
        pan[x][j] = 1 if(pan[x][j] == 0) else 0
        pan[j][y] = 1 if(pan[j][y] == 0) else 0

for i in range(panSize):
    for j in range(panSize):
        print(pan[i][j], end=" ")
    print()