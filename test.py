from math import sqrt
upper_limit = 10000
hexs = set()
while len(hexs) < 2:
    tris = {n*(n+1)//2 for n in range(2, upper_limit)}
    pents = {v for n in range(upper_limit) if (v := n*(3*n-1)//2) in tris}
    hexs = {v for n in range(upper_limit) if (v:= n*(2*n-1)) in pents}
    upper_limit *= 10

print(hexs)
# 1533776805

n=(1+sqrt(1+8*1533776805))/4
print(n)