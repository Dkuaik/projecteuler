# este problema consiste en encontrar la suma de todos los números amigables menores a 10000
# un numero amigable es un número entero positivo que es igual a la suma de sus divisores propios positivos
# un par de numeros amigables son dos números enteros positivos a y b tales que la suma de los 
# divisores propios de uno es igual al otro y viceversa

import Modulos as md

num_a=[]
for i in range (1,10000):
    sum_pd=0
    pd=md.properDivisors(i)
    sum_pd=sum(pd)
    if sum(md.properDivisors(sum_pd))==i and i!=sum_pd:
        print(f"{i} y {sum_pd} son numeros amigos")
        num_a.append(i)
        i=sum_pd

print(sum(num_a))