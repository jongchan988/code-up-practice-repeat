a, r, n = input().split()

# 시작값
a = int(a)

# 등비
r = int(r)

# ?번째
n = int(n)

for i in range(n-1):
    a = a * r
    
print(a)
