n = int(input())
checkNumArr = [3, 6, 9]

for i in range(1, n+1) :
    result = ''
    for j in range (0, len(str(i))):
        value = str(i)
        if (int(value[j]) in checkNumArr):
            result = result + "X"

    print(result if (result != '') else i, end=' ')
