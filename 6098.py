x,y = [1,1]
size = 10
pan = [[0] * size for _ in range(size)]

for i in range(size):
    inputArr = input().split()
    for j in range(size):
        pan[i][j] = int(inputArr[j])

pan[x][y] = 9

while(True):
    if(pan[x][y+1] == 0 or pan[x][y+1] == 2):
        y = y + 1
    elif (pan[x+1][y] == 0 or pan[x+1][y] == 2):
        x = x + 1
    else:
        break
    nextValue = pan[x][y]
    pan[x][y] = 9
    if (nextValue == 2):
        break
    


for i in range(size):
    for j in range(size):
        print(pan[i][j], end=" ")
    print()