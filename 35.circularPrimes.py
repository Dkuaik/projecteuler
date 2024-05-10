# Euler 35: Números circulares primos
# Un número circular primo es un número que sigue siendo primo
# al rotar sus dígitos. Ejemplo: 197, 971, 719 son todos primos.
# Encuentra cuántos números circulares primos hay por debajo de un millón

#definicion de funcion para rotar digitos

import Modulos as md
import time
start=time.time()
primoCircular=set()
rotaciones=[]
def rotate(n):
    n=str(n)
    return int(n[-1]+n[:-1])
i=1
while i<1000000:
    if not md.esPrimo(i):
        i+=1
        continue
    if i in primoCircular:
        i+=1
        continue
    i_temp=i
    for j in range(len(str(i))):
        rotaciones.append(i_temp)
        i_temp=rotate(i_temp)
    if all([md.esPrimo(x) for x in rotaciones]):
        for x in rotaciones:
            primoCircular.add(x)
    # print(rotaciones)
    # i=rotate(i)
    rotaciones=[]
    i+=1
end=time.time() 
print(end-start)
primoCircular=sorted(list(primoCircular))
print(len(primoCircular))