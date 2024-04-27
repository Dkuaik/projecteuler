# este problema consiste en calcular la suma de los dígitos de 100!

import Modulos as md

n=md.factorial(100)
n=str(n)
sum=0
for i in n:
    sum+=int(i)
print(sum)