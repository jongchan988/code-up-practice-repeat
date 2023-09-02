h, w = input().split()
n = int(input())


h = int(h)
w = int(w)


pan = [[0] * h for _ in range(w)]

for _ in range(n):
    l, d, x, y = input().split()
    l = int(l)
    d = int(d)
    x = int(x) - 1
    y = int(y) - 1
    for i in range(l):
        targetX = x
        targetY = y
        if (d == 1) :
            targetX = targetX + i
        else:
            targetY = targetY + i
        pan[targetX][targetY] = 1

for i in range(h):
    for j in range(w):
        print(pan[i][j], end = " ")
    print()