# este programa tiene que sumar los digitos de 2^1000

num=2**1000
sum=0
for i in str(num):
    sum+=int(i)
print(sum)