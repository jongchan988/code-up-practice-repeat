n = int(input())
a = input().split()

result = 10001

for i in range(n):
    value = int(a[i])
    if result > value:
        result = value