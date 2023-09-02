panStart = 1
panEnd = 19

n = int(input())
pan = []

for i in range(panEnd + 1):
    pan.append([])
    for j in range(panEnd + 1):
        pan[i].append(0)

for i in range(n):
    x, y = input().split()
    pan[int(x)][int(y)] = 1

for i in range(panStart, panEnd + 1):
    for j in range(panStart, panEnd + 1):
        print(pan[i][j], end=" ")
    print()