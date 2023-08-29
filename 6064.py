a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

result = a
check_arr = [b, c]


for num in check_arr:
    result = result if (result < num) else num
    

print(result)