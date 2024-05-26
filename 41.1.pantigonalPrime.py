# para resolver el problema de forma eficiente recorremos sobre las permutaciones de los 
# conjuntos que forman numero pantigonales.

import Modulos as md #importo mis funciones para generar las permutaciones

for i in range(1,10):
    conjuntoDigitos=[i for i in range(1,i+1)]
    permutaciones=md.permutations(conjuntoDigitos)
    for j in permutaciones:
        permutacion=list(map(str,j))
        permutacionNum=int(''.join(permutacion))
        if md.isPrime(permutacionNum):
            maxPP=permutacionNum
            # print(maxPP, " este es primo")
print(maxPP)
# Respuesta: 7652413