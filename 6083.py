result = 0
r, g, b = input().split()

r = int(r)
g = int(g)
b = int(b)

for i in range(0, r):
    for j in range(0, g):
        for k in range(0, b):
            result = result + 1
            print(i, j, k, sep=' ')
print(result)