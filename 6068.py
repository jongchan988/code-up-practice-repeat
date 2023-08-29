n = int(input())

def getGrade(num):
    if (90 <= n):
        return 'A'
    elif (70 <= n):
        return 'B'
    elif (40 <= n):
        return 'C'
    else :
        return 'D'    

print(getGrade(n))
