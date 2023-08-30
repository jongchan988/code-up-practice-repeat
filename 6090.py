a, m, d, n = input().split()

# 시작값
a = int(a)

# 곱할값
m = int(m)

# 더할값
d = int(d)

# ?번째
n = int(n)

for i in range(n-1):
    a = a * m + d
    
print(a)
