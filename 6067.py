num = int(input())

def isEven(n):
    return n % 2 == 0

if num < 0:
    if isEven(num):
        print('A')
    else:
        print('B')
else:
    if isEven(num):
        print('C')
    else:
        print('D')